import os
import json
import botocore
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
        client = s3.meta.client
        # Loop over each file in the parent and upload individually
        for root,dirs,files in os.walk(path_to_files):
            for file in files:
                file_path = "{}/{}".format(path_to_files, file)
                print("Uploading {}............".format(file_path))
                obj = s3.Object(self.s3_bucket, file)
                obj.put(Body=open(file_path, 'rb'), ContentType='text/html')
        # Make files public so website will work correctly
        bucket = s3.Bucket(self.s3_bucket)
        self.setup_bucket_policy()
        print("Upload complete!")


    def setup_bucket_site(self):
        s3 = self.session.resource('s3')
        response = s3.meta.client.put_bucket_website(
            Bucket=self.s3_bucket,
            WebsiteConfiguration={
                'ErrorDocument': {
                    'Key': '404.html'
                },
                'IndexDocument': {
                    'Suffix': 'index.html'
                }
            }
        )

    def setup_bucket_policy(self):
        s3 = self.session.resource('s3')
        client = s3.meta.client
        policy = json.dumps({
            "Version":"2012-10-17",
            "Statement":[{
                "Sid":"AddPerm",
                "Effect":"Allow",
                "Principal": "*",
                "Action":["s3:GetObject"],
                "Resource":["arn:aws:s3:::" + self.s3_bucket + "/*"]
            }]
        })
        response = client.put_bucket_policy(
                Bucket=self.s3_bucket,
                Policy=policy
        )


    def create_cloudfront_distro(self):
        pass

    def invalidate_cache(self):
        pass
