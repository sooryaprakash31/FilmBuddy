import os

from .data_service import DatasetService
from ..config import MOVIES_DATASET_FILE_PATH, RATINGS_DATASET_FILE_PATH, STORAGE_TYPE
from ..services.storage_service import StorageService


class InitializerService:

    def __init__(self):
        pass

    @staticmethod
    def initialize():
        print("Starting the application. Please wait..")

        if STORAGE_TYPE == "s3":
            storage_service = StorageService()
            print("Downloading datasets...", flush=True)
            storage_service.download_all_data()
            print("Downloaded successfully!", flush=True)
        elif STORAGE_TYPE == "local":
            if not os.path.exists(MOVIES_DATASET_FILE_PATH):
                raise Exception("Movies dataset file is not present in datasets directory")
            if not os.path.exists(RATINGS_DATASET_FILE_PATH):
                raise Exception("Ratings dataset file is not present in datasets directory")

        print("Loading datasets...", flush=True)
        DatasetService(movies_dataset_file_path=MOVIES_DATASET_FILE_PATH,
                       ratings_dataset_file_path=RATINGS_DATASET_FILE_PATH)
        print("Loaded successfully!", flush=True)
