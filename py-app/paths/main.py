import os
import sys

SUB_DIR_LIST = [
    'Data',
    'Logs'
]

SUB_DIRS = {}   # container of dirs, will load by code below

if getattr( sys, 'frozen', False ):
    # running in a bundle
    user_data_base = os.path.basename(os.getcwd())
else:
    # running live
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    pkg_json_path = os.path.join(project_root, 'package.json')
    import json
    with open(pkg_json_path, 'r') as pkg_json_file:
        pkg_info = json.load(pkg_json_file)
    product_name = pkg_info['productName']
    user_data_base = '%s_DEV' % product_name

user_data_path = os.path.join('C:/AppData', user_data_base)

def generate_sub_dirs(user_data_path):
    print('USER DATA: %s' % user_data_path)
    for i in SUB_DIR_LIST:
        sub_dir = os.path.join(user_data_path, i)
        SUB_DIRS[i] = sub_dir
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)


def get_sub_dir(key):
    return SUB_DIRS[key]


generate_sub_dirs(user_data_path)