import os
import click

from .core import load_config
from .aws_helper import AWSClient


@click.command()
@click.argument('path', type=click.Path(exists=True))
def deploy(path):

    path = os.path.abspath(path)
    cfg = load_config(path)
    aws = AWSClient(**cfg)

    click.echo('Syncing project...')
    aws.s3.sync(path)
    aws.s3.configure_policy()

    click.echo('Configuring website...')
    aws.s3.configure_site()

    click.echo('Deploy complete!')
    click.echo(f'http://{aws.bucket}.s3-website-{aws.region}.amazonaws.com')


if __name__ == '__main__':
    deploy()
