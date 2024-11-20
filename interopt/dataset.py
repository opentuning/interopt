import os
import logging
import pandas as pd
import requests
from typing import Optional


class TabularDataset:
    def __init__(self, benchmark_name, dataset, parameter_names, objectives, enable_download):
        self.objectives = objectives
        self.tab = None
        self.base_url = "https://raw.githubusercontent.com/odgaard/bacobench_data/main"
        self.parameter_names = parameter_names
        self.tab_path = f'datasets/{benchmark_name}_{dataset}.csv'
        if os.path.exists(self.tab_path) or (enable_download and self.ensure_dataset_downloaded()):
            self.tab = pd.read_csv(self.tab_path).dropna()
        self.prepare_dataset()

    def prepare_dataset(self):
        if self.tab is None:
            multi_index = pd.MultiIndex.from_tuples([], names=self.parameter_names)
            self.tab = pd.DataFrame(
                columns=self.parameter_names + self.objectives,
                index=multi_index)
        else:
            self.tab.set_index(self.parameter_names, inplace=True)
            self.tab.sort_index(inplace=True)
        self.query_tab = self.tab.copy()

    def ensure_dataset_downloaded(self) -> bool:
        if not os.path.exists('datasets'):
            os.makedirs('datasets')
        if not os.path.exists(self.tab_path):
            url = f"{self.base_url}/{os.path.basename(self.tab_path)}"
            return self.download_file(url, self.tab_path)
        return False

    @staticmethod
    def download_file(url: str, local_file_path: str) -> bool:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(local_file_path, 'wb') as f:
                f.write(response.content)
            logging.info(f"Downloaded {local_file_path}")
            return True
        except requests.exceptions.RequestException as e:
            logging.warning(f"Failed to download {url}: {e}")
            return False

    def query(self, query_dict, fidelity_dict) -> Optional[pd.Series]:
        d = query_dict.copy()
        d.update(fidelity_dict)
        query_tuple = tuple(d[col] for col in self.query_tab.index.names)
        if query_tuple in self.query_tab.index:
            print("Using tabular data")
            query_result: pd.Series = self.query_tab.loc[query_tuple][self.objectives]
            return query_result
        return None

    def write(self, result):
        file_exists = os.path.isfile(self.tab_path)
        write_result = result.reset_index()
        write_result.to_csv(self.tab_path,
                            mode='a' if file_exists else 'w', sep=",",
                            index=False, header=not file_exists)

    def add(self, result):
        self.write(result)
        logging.info(f"Adding to tabular data: {result}")
        self.query_tab = pd.concat([self.query_tab, result])
