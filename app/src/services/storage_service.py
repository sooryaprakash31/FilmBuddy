import os
import zipfile
from io import BytesIO

import boto3

from ..config import (
    ROOT_DIR,
    BUCKET_NAME,
    REGION_NAME,
    ACCESS_KEY_ID,
    SECRET_ACCESS_KEY,
    APP_ROOT_DIR, DATASETS_DIR
)


class StorageService:
    """
    S3 storage related methods
    """

    def __init__(self):
        self.secret_key = SECRET_ACCESS_KEY
        self.bucket_name = BUCKET_NAME
        self.access_key = ACCESS_KEY_ID
        self.region = REGION_NAME
        self.root_dir = ROOT_DIR

        self.storage_client = boto3.resource('s3',
                                             aws_access_key_id=self.access_key,
                                             aws_secret_access_key=self.secret_key,
                                             region_name=self.region)

    def download_all_data(self):

        """
        This method is used to download all the datasets from a directory in S3 Bucket
        and extract them in local storage
        """

        # List objects in the specified S3 directory
        bucket = self.storage_client.Bucket(self.bucket_name)
        for obj in bucket.objects.filter(Prefix=self.root_dir):
            # Check if the object is a file (not a directory)
            if not obj.key.endswith('/'):
                # Create the local directory structure if it doesn't exist
                local_path = os.path.join(APP_ROOT_DIR, os.path.dirname(obj.key))
                os.makedirs(local_path, exist_ok=True)

                # Download the S3 object
                s3_object = self.storage_client.Object(self.bucket_name, obj.key)
                object_data = s3_object.get()['Body'].read()

                # Unzip the file if it's a zip archive
                if obj.key.endswith('.zip'):
                    with zipfile.ZipFile(BytesIO(object_data)) as zip_file:
                        zip_file.extractall(local_path)
                else:
                    # Save the object as-is if it's not a zip file
                    local_file_path = os.path.join(APP_ROOT_DIR, DATASETS_DIR, obj.key)
                    with open(local_file_path, 'wb') as local_file:
                        local_file.write(object_data)
