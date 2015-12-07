import os
import boto3
from boto3.session import Session


class AWSHelper(object):

    def __init__(self, s3_access_key, s3_secret_key,
                 s3_bucket, cloudfront_distribution_id):
        self.s3_access_key = s3_access_key
        self.s3_secret_key = s3_secret_key
        self.s3_bucket = s3_bucket
        self.session = Session (
            aws_access_key_id=s3_access_key,
            aws_secret_access_key=s3_secret_key,
            region_name='us-east-1'
        )


    def upload_files_to_s3(self, path_to_files):
        s3 = self.session.resource('s3')
        # Loop over each file in the parent and upload individually
        for root,dirs,files in os.walk(path_to_files):
            for file in files:
                file_path = "{}/{}".format(path_to_files, file)
                print("Uploading {}............".format(file_path))
                s3.Object(self.s3_bucket, file).put(Body=open(file_path, 'rb'))
        print("Upload complete!")

    def create_cloudfront_distro(self):
        pass

    def invalidate_cache(self):
        pass
