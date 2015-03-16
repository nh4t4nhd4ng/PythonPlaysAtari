#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Will Brennan'

# built-in libarys
import sys
import logging
import argparse
import datetime
# Standard libaries
# Custom libaries

logger = logging.getLogger('main')


def get_args(default=None, args_string=''):
    """
    This function gets the command line arguments and passes any unknown arguments to ALE.
    :param default: dictionary of default arguments with keys as `dest`
    :return: command line arguments
    """
    if not default:
        default = {}
    assert isinstance(default, dict), 'default_dict must be a dictionary of default arguments'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-d', '--display', dest='display', default=default.get('display', True), type=bool, help="display Game while learning and testing")
    parser.add_argument('-t', '--trained', dest='name', default=default.get('name', ''), type=str, help='folderpath to trained network')
    parser.add_argument('-i', '--improvement', dest='improvement', action='store_true', help='display improvement over epochs')
    if args_string:
        args_string = args_string.split(' ')
        args = parser.parse_args(args_string)
    else:
        args = parser.parse_args()
    return args


class DataTests(object):
    def __init__(self, args):
        self.args = args

    def speed_tests(self):
        pass

    def process(self):
        pass


if __name__ == '__main__':
    args = get_args()
    logger.setLevel(logging.INFO)
    fh, ch = logging.FileHandler('watch_{0}.log'.format(args.name)), logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
    for i in [fh, ch]:
        i.setLevel(logging.INFO)
        i.setFormatter(formatter)
        logger.addHandler(i)
    tests = DataTests(args)
    tests.process()

