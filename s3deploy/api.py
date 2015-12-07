import os
import yaml


def read_config():
    print(contents)


def read_config_file():
    current_dir = os.getcwd()
    config_path = current_dir + '/s3Deploy.cfg'
    with open(config_path, 'r') as f:
        contents = yaml.load(f)
        print(contents)

if __name__ == "__main__":
    read_config_file()
