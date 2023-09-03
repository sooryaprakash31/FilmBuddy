import os.path

import pandas as pd

from ..config import APP_ROOT_DIR, DATASETS_DIR


class DataService:
    """
    Dataset related methods
    """

    def __init__(self, dataset_file_name: str, dataset_file_extension: str = "csv"):
        self.dataset_file_name = dataset_file_name
        self.dataset_file_extension = dataset_file_extension

    def get_dataframe(self):
        """
        This method is used to get the dataframe from the datasource
        :return: dataframe of the dataset
        """
        df = self.load_data()
        return df

    def load_data(self):
        """
        This method is used to load the dataset into a dataframe
        :return:
        """
        dataset_file_path = os.path.join(APP_ROOT_DIR, DATASETS_DIR,
                                         f"{self.dataset_file_name}.{self.dataset_file_extension}")
        df = pd.read_csv(dataset_file_path)
        return df
