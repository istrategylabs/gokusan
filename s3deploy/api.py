import os
import yaml

from aws_helper import Config


def read_config_file():
    current_dir = os.getcwd()
    config_path = current_dir + '/s3Deploy.cfg'
    try:
        with open(config_path, 'r') as f:
            contents = yaml.load(f)
            print(contents)
    except OSError:
        print("s3Deploy configuration file not found.")

if __name__ == "__main__":
    read_config_file()
