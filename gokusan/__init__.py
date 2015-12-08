from .cli import main


#! /usr/bin/env python

""" gokusan main file """
import pkg_resources

__author__ = "Julian Gindi"
__email__ = "julian@isl.co"
__version__ = pkg_resources.get_distribution('gokusan').version

from gokusan.cli import main

if __name__ == '__main__':
    main()
