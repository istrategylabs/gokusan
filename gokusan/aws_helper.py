import os
import json
from boto3.session import Session


class CloudfrontClient():

    def __init__(self, client):
        self.client = client

    def create_distro(self):
        pass

    def invalidate_cache(self):
        pass


class S3Client():

    def __init__(self, client):
        self.client = client

    def sync(self, path):
        bucket_url = f's3://{self.client.bucket}'
        command_string = \
            f'AWS_ACCESS_KEY_ID={self.client.access_key} ' + \
            f'AWS_SECRET_ACCESS_KEY={self.client.secret_key} ' + \
            f'aws s3 sync {path} {bucket_url} ' + \
            '--exclude gokusan.yml --acl public-read'
        os.system(command_string)

    def configure_policy(self):
        policy = json.dumps({
            'Version': '2012-10-17',
            'Statement': [{
                'Sid': 'AddPerm',
                'Effect': 'Allow',
                'Principal': '*',
                'Action': ['s3:GetObject'],
                'Resource': [
                    f'arn:aws:s3:::{self.client.bucket}/*',
                ]
            }]
        })
        s3 = self.client.session.resource('s3')
        s3.meta.client.put_bucket_policy(
            Bucket=self.client.bucket, Policy=policy)

    def configure_site(self):
        s3 = self.client.session.resource('s3')
        bucket_website = s3.BucketWebsite(self.client.bucket)
        bucket_website.put(
            WebsiteConfiguration={
                'ErrorDocument': {
                    'Key': '404.html'
                },
                'IndexDocument': {
                    'Suffix': 'index.html'
                }
            }
        )


class AWSClient(object):

    def __init__(self, access_key, secret_key, bucket):
        self.region = 'us-east-1'
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket = bucket
        self.session = Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=self.region
        )

        self.cloudfront = CloudfrontClient(self)
        self.s3 = S3Client(self)
