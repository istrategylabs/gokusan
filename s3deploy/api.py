import sys
import os
import yaml

from aws_helper import AWSHelper


def read_config_file():
    current_dir = os.getcwd()
    config_path = current_dir + '/s3Deploy.cfg'
    try:
        with open(config_path, 'r') as f:
            contents = yaml.load(f)
            return contents
    except OSError:
        print("s3Deploy configuration file not found.")
        sys.exit(0)

if __name__ == "__main__":
    cfg = read_config_file()
    h = AWSHelper(**cfg)
    h.upload_files_to_s3('./test_files')
    print("Deploy complete!")
