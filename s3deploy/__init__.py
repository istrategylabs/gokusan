from .cli import main


#! /usr/bin/env python

""" s3deploy main file """
import pkg_resources

__author__ = "Julian Gindi"
__email__ = "julian@isl.co"
__version__ = pkg_resources.get_distribution('s3deploy').version

from s3deploy.cli import main

if __name__ == '__main__':
    main()
