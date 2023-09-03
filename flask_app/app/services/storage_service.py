import boto3

from ..config import (
    ROOT_DIR,
    BUCKET_NAME,
    REGION_NAME,
    ACCESS_KEY_ID,
    SECRET_ACCESS_KEY
)


class StorageService:

    def __init__(self):
        self.secret_key = SECRET_ACCESS_KEY
        self.bucket_name = BUCKET_NAME
        self.access_key = ACCESS_KEY_ID
        self.region = REGION_NAME
        self.root_dir = ROOT_DIR

        self.storage_client = boto3.client('s3',
                                           aws_access_key_id=self.access_key,
                                           aws_secret_access_key=self.secret_key,
                                           region_name=self.region)

    def download_data(self, cloud_path, local_path):

        print("Download started", flush=True)
        self.storage_client.download_file(self.bucket_name, cloud_path, local_path)
        print("Download done", flush=True)
