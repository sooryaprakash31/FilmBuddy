import pandas as pd


class DataService:
    """
    Dataset related methods
    """

    def __init__(self, dataset_name):
        self.dataset_name = dataset_name

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
        df = pd.read_csv(f'/app/assets/{self.dataset_name}.csv')
        return df
