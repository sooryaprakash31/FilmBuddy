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
