import sys
import os
import yaml

from .aws_helper import AWSHelper


def read_config_file():
    current_dir = os.getcwd()
    config_path = current_dir + '/gokusan.cfg'
    try:
        with open(config_path, 'r') as f:
            contents = yaml.load(f)
            return contents
    except OSError:
        print('gokusan configuration file not found.')
        sys.exit(0)

def main():
    cfg = read_config_file()
    h = AWSHelper(**cfg)
    h.upload_files_to_s3('./test_files')
    print('Configuring bucket website...')
    h.setup_bucket_site()
    print('Deploy complete!')
