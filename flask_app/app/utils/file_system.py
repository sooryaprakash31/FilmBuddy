import os

from ..config import APP_ROOT_DIR


def get_local_path(dir_name):
    return os.path.join(APP_ROOT_DIR, dir_name)
