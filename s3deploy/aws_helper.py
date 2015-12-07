import boto3

class AWSHelper(object):

    def __init__(self):
        self.client = boto3.client('s3', 'us-east-1')

def upload_files_to_s3(bucket_name):
    file_path = './test_files'

def create_cloudfront_distro(bucket_name):
    pass

def invalidate_cache(cloudfront_distro):
    pass
