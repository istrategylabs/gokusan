import os

import yaml


def load_config(path):
    config_path = os.path.join(path, 'gokusan.yml')
    if not os.path.exists(config_path):
        raise ValueError('gokusan configuration file not found')
    with open(config_path, 'r') as f:
        contents = yaml.load(f)
        return contents
