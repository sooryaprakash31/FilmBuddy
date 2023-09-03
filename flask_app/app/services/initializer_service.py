from .data_service import DatasetService
from ..config import MOVIES_DATASET_FILE_PATH, RATINGS_DATASET_FILE_PATH
from ..services.storage_service import StorageService


class InitializerService:

    def __init__(self):
        pass

    @staticmethod
    def initialize():
        storage_service = StorageService()
        print("Downloading datasets...", flush=True)
        storage_service.download_all_data()
        print("Downloaded successfully!", flush=True)

        print("Loading datasets...", flush=True)
        DatasetService(movies_dataset_file_path=MOVIES_DATASET_FILE_PATH,
                       ratings_dataset_file_path=RATINGS_DATASET_FILE_PATH)
        print("Loaded successfully!", flush=True)
