from typing import Optional
import pandas as pd
import numpy as np
import asyncio
import random
import ast
import logging

from interopt.runner.grpc_runner import run_config
from interopt.runner.model import load_models
from interopt.definition import ProblemDefinition
from interopt.dataset import TabularDataset
from interopt.queue_handler import QueueHandler

class SoftwareQuery:
    def __init__(self, benchmark_name, dataset,
                 parameter_names, tabular_dataset, enabled_objectives,
                 enable_tabular, enable_model, fidelity_names=None):
        self.tabular_dataset = tabular_dataset
        if fidelity_names is None:
            fidelity_names = []

        if enable_model:
            self.models = load_models(
                self.tabular_dataset.query_tab, benchmark_name, dataset,
                enabled_objectives, parameter_names + fidelity_names)
        self.query_tab = self.tabular_dataset.query_tab
        self.enable_tabular = enable_tabular
        self.enable_model = enable_model

    async def query_software(self, query_dict: dict, fidelity_dict: dict, study_id: str) -> Optional[pd.DataFrame]:
        query_result = pd.DataFrame()
        if self.enable_tabular:
            query_result = self.tabular_dataset.query(query_dict, fidelity_dict)
        if query_result is None and self.enable_model:
            query_result: pd.Series = self.query_model(query_dict, fidelity_dict)
        return query_result

    def query_model(self, query_dict, fidelity_dict) -> pd.Series:
        if "permutation" in query_dict.keys():
            model_query_dict = self.convert_permutation_to_tuple(query_dict, 'permutation')
        else:
            model_query_dict = query_dict
        model_query_dict.update(fidelity_dict)

        objectives = self.tabular_dataset.objectives
        print("Using surrogate model")
        results = [self.models[objective].predict(pd.DataFrame([model_query_dict]))[0]
                   for objective in objectives]

        # Convert from log scale back to normal
        results = [np.exp(result) for result in results]

        return pd.DataFrame(
            [results], columns=objectives,
            index=[tuple(list(query_dict.values()) + list(fidelity_dict.values()))]).iloc[0]

    def convert_permutation_to_tuple(self, query_dict: dict, param: str) -> list[int]:
        new_dict = query_dict.copy()
        tuple_str = ast.literal_eval(new_dict[param])
        for i, value in enumerate(tuple_str):
            new_dict[f'tuple_{param}_{i}'] = value
        del new_dict[param]
        return new_dict

class GRPCForwarder:
    def __init__(self, server_addresses, port, ports, enabled_objectives, definition: ProblemDefinition):
        self.definition = definition
        self.parameters = definition.search_space.params
        self.fidelity_params = definition.search_space.fidelity_params
        self.enabled_objectives = enabled_objectives
        self.grpc_urls = self.calculate_grpc_urls(server_addresses, port, ports)
        self.queue_handler = QueueHandler(self.grpc_urls)

    def calculate_grpc_urls(self, server_addresses, port, ports):
        logging.info(f"Server addresses: {server_addresses}, port: {port}, ports: {ports}")
        if server_addresses is None:
            return ["localhost:50051"]
        if server_addresses and port and ports is None:
            return [f"{server_address}:{port}" for server_address in server_addresses]
        if server_addresses and port is None and ports is None:
            port = 50051
            return [f"{server_address}:{port}" for server_address in server_addresses]
        if server_addresses and ports:
            if len(server_addresses) != len(ports):
                raise ValueError("Server addresses and ports should have the same length")
            return [f"{server_addresses[i]}:{ports[i]}" for i in range(server_addresses)]
        return [] # TODO: Implement this

    async def query_hardware(self, query: dict, fidelities: dict, study_name: str) -> pd.DataFrame:
        # Implement or override as needed
        result = await self.send_query(query, fidelities, study_name)
        result = await self.process_grpc_results(result, query, fidelities)
        return result

    async def send_query(self, query: dict, fidelities: dict, study_name: str) -> dict:
        url = await self.queue_handler.get_available_server_url()
        print(f"Using hardware: {url}")
        try:
            result = await run_config(query, self.parameters, fidelities, self.fidelity_params, url)
            return result
        finally:
            await self.queue_handler.mark_server_as_available(url)

    async def process_grpc_results(
            self, result: dict, query: dict, fidelities: dict) -> pd.DataFrame:
        # Create a MultiIndex with names
        d = query.copy()
        d.update(fidelities)
        index_tuples = [tuple(d.values())]  # This will be a list of tuples

        if len(result) == 0:
            # Creating a MultiIndex without rows initially
            multi_index = pd.MultiIndex.from_tuples([], names=list(d.keys()))

            # Creating an empty DataFrame with a MultiIndex and specific columns
            return pd.DataFrame(columns=self.enabled_objectives, index=multi_index)

        values = [result[e][0] for e in self.enabled_objectives]
        multi_index = pd.MultiIndex.from_tuples(index_tuples, names=list(d.keys()))
        return pd.DataFrame([values], columns=self.enabled_objectives, index=multi_index)


class Study():
    tab = None
    query_tab = None
    models = None

    def __init__(self, benchmark_name: str, definition: ProblemDefinition,
                 enable_tabular: bool, dataset, enabled_objectives: list[str],
                 server_addresses: list[str] = None, port=None, ports=None, url="", queue_handler=None,
                 enable_model: bool = True, enable_download: bool = True, study_name = None):
        self.benchmark_name = benchmark_name
        self.enabled_objectives = enabled_objectives
        self.enable_tabular = enable_tabular
        self.enable_model = enable_model
        self.dataset = dataset
        self.definition = definition
        self.trajectory = []
        self.study_name = study_name if study_name else f"{benchmark_name}_{dataset}_{random.randint(0, 100000)}"

        fidelity_names = [param.name for param in definition.search_space.fidelity_params]
        parameter_names = [param.name for param in definition.search_space.params]
        self.tabular_dataset = TabularDataset(
            benchmark_name, dataset, parameter_names + fidelity_names,
            enabled_objectives, enable_download)

        if self.enable_tabular or self.enable_model:
            self.software_query = SoftwareQuery(
                benchmark_name, dataset,
                parameter_names=parameter_names,
                tabular_dataset=self.tabular_dataset,
                enabled_objectives=self.enabled_objectives,
                enable_tabular=self.enable_tabular,
                enable_model=self.enable_model,
                fidelity_names=fidelity_names)
        else:
            self.software_query = None
        self.grpc_query = GRPCForwarder(
            server_addresses, port, ports, self.enabled_objectives, self.definition)

    def set_tabular(self, enable_tabular: bool):
        self.enable_tabular = enable_tabular

    def get_enabled_objectives(self):
        return self.enabled_objectives

    def query(self, query: dict, fidelities: Optional[dict] = None) -> dict:
        return asyncio.run(self.query_async(query, fidelities))

    async def query_async(self, query: dict, fidelities: Optional[dict] = None,
                          study_name=None) -> list[dict]:
        if study_name is None:
            study_name = self.study_name
        if fidelities is None:
            fidelities = {}
        res = await self.query_choice(query, fidelities, study_name)
        ret = {}
        for k in self.enabled_objectives:
            ret[k] = res[k]
        return ret

    async def query_choice(self, query: dict, fidelities: dict, study_name: str) -> dict:
        result = None
        if self.enable_tabular:
            result = await self.software_query.query_software(
                query.copy(), fidelities.copy(), study_name)
            if isinstance(result, pd.Series):
                result = result.to_frame().T
        if result is None:
            print("Using hardware")
            result = await self.grpc_query.query_hardware(
                query.copy(), fidelities.copy(), study_name)
            self.tabular_dataset.add(result)
        print(result, type(result))
        if len(result.index) == 0:
            return { "compute_time": 0.0 }

        return result.iloc[0].to_dict()
