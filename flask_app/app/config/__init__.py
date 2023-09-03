import os

from ..utils.env import get_env

ROOT_DIR = get_env("ROOT_DIR")
ACCESS_KEY_ID = get_env("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = get_env("SECRET_ACCESS_KEY")
REGION_NAME = get_env("REGION_NAME")
BUCKET_NAME = get_env("BUCKET_NAME")

# APP_ROOT_DIR = os.path.dirname(os.path.abspath(os.path.abspath(os.path.abspath(__file__))))
APP_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATASETS_DIR = "datasets"
