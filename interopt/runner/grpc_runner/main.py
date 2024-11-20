import ast
import grpc.aio
import logging
from interopt.parameter import (
    Integer, Real, String, Categorical, Ordinal, Permutation,
)
import interopt.runner.grpc_runner.config_service_pb2 as cs
import interopt.runner.grpc_runner.config_service_pb2_grpc as cs_grpc
import interopt.runner.grpc_runner.interopt_service_pb2 as ios
import interopt.runner.grpc_runner.interopt_service_pb2_grpc as ios_grpc

def value_to_param(value, param):
    if isinstance(param, Integer):
        return cs.Parameter(integer_param=cs.IntegerParam(value=int(value)))
    
    if isinstance(param, Real):
        return cs.Parameter(real_param=cs.RealParam(value=float(value)))

    if isinstance(param, Ordinal):
        return cs.Parameter(ordinal_param=cs.OrdinalParam(value=int(value)))

    if isinstance(param, Categorical):
        return cs.Parameter(categorical_param=cs.CategoricalParam(value=int(value)))

    if isinstance(param, String):
        return cs.Parameter(string_param=cs.StringParam(value=str(value)))

    if isinstance(param, Permutation):
        tuple_value = ast.literal_eval(value)
        return cs.Parameter(permutation_param=cs.PermutationParam(values=list(tuple_value)))

    raise ValueError(f"Unknown parameter type: {param.__class__.__name__}")

async def run_config(query_dict: dict, parameters: list, fidelity_dict: dict, fidelities: list, grpc_url: str, study_name: str = ""):
    parameter_dict = {param.name: param for param in parameters}
    query_dict_grpc = {
        name: value_to_param(value, parameter_dict[name])
        for name, value in query_dict.items()
    }

    config = cs.Configuration(parameters=query_dict_grpc)

    if fidelities:
        fidelity_param_dict = {param.name: param for param in fidelities}
        fidelity_dict_grpc = {
            name: value_to_param(value, fidelity_param_dict[name])
            for name, value in fidelity_dict.items()
        }
    else:
        fidelity_dict_grpc = {}

    fidelities_grpc = cs.Fidelities(parameters=fidelity_dict_grpc)
    result = {}

    async with grpc.aio.insecure_channel(grpc_url) as channel:
        stub = cs_grpc.ConfigurationServiceStub(channel)
        request = cs.ConfigurationRequest(
            configurations=config,
            output_data_file="",
            study_name=study_name,
            fidelities=fidelities_grpc
        )
        logging.info(f"Sending request: {request}")
        try:
            response = await stub.RunConfigurationsClientServer(request)
            logging.info(f"Received response: {response}")
            for metric in response.metrics:
                result[metric.name] = metric.values
        except grpc.aio.AioRpcError as e:
            logging.error(f"GRPC error: {e.details()}")
            logging.error(f"Status code: {e.code()}")

    return result


async def setup_study(study_name: str, problem_name: str,
                      dataset: str, enable_tabular: bool, enable_model: bool,
                      enable_download: bool, enabled_objectives: list[str],
                      server_addresses: list[str], server_port: int,
                      interopt_address: str, interopt_port: int):
    request = ios.SetupStudyRequest(
        study_name=study_name,
        problem_name=problem_name,
        dataset=dataset,
        enable_tabular=enable_tabular,
        enable_model=enable_model,
        enable_download=enable_download,
        enable_objectives=enabled_objectives,
        server_connections=[
            ios.ServerConnection(server_address=server_addresses[i], server_port=server_port) 
            for i in range(len(server_addresses))]
    )

    grpc_url = f"{interopt_address}:{interopt_port}"

    async with grpc.aio.insecure_channel(grpc_url) as channel:
        stub = ios_grpc.InteroptServiceStub(channel)
        logging.info(f"Sending request: {request}")
        response = await stub.SetupStudy(request)
        logging.info(f"Received response: {response}")
        return response
