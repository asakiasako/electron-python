import os.path

DATA_ROOT_DIR = 'C:/AppData'
APP_DIR = os.getcwd()
APP_NAME = os.path.basename(APP_DIR)
APP_DATA_DIR = os.path.abspath(os.path.join(DATA_ROOT_DIR, APP_NAME))

SUB_DIR_LIST = [
    'Data',
    'Logs'
]

SUB_DIRS = {}   # container of dirs, will load by code below

for i in SUB_DIR_LIST:
    sub_dir = os.path.join(APP_DATA_DIR, i)
    SUB_DIRS[i] = sub_dir
    if not os.path.exists(sub_dir):
        os.makedirs(sub_dir)


def get_sub_dir(key):
    return SUB_DIRS[key]