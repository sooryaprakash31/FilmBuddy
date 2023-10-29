import pandas as pd


class DatasetService:
    """
    Datasets related methods
    Follows singleton pattern to maintain only one instance of the dataset throughout the application
    """
    _instance = None
    _movies_dataset = None
    _ratings_dataset = None

    def __new__(cls, movies_dataset_file_path, ratings_dataset_file_path):
        if cls._instance is None:
            cls._instance = super(DatasetService, cls).__new__(cls)
            cls._movies_dataset = cls._load_dataset(movies_dataset_file_path)
            cls._ratings_dataset = cls._load_dataset(ratings_dataset_file_path)
        return cls._instance

    @staticmethod
    def _load_dataset(dataset_file_path):
        df = pd.read_csv(dataset_file_path)
        return df

    def get_movies_dataset(self):
        return self._movies_dataset

    def get_ratings_dataset(self):
        return self._ratings_dataset
