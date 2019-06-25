import os
import sys

SUB_DIR_LIST = [
    'Data',
    'Logs'
]

SUB_DIRS = {}   # container of dirs, will load by code below

user_data_path = os.environ['userDataPath']

def generate_sub_dirs(user_data_path):
    print('RPCServer USER DATA: %s' % user_data_path)
    for i in SUB_DIR_LIST:
        sub_dir = os.path.join(user_data_path, i)
        SUB_DIRS[i] = sub_dir
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)


def get_sub_dir(key):
    return SUB_DIRS[key]


generate_sub_dirs(user_data_path)