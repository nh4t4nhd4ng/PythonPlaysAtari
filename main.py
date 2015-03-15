#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Will Brennan'

# built-in libarys
import sys
import logging
import argparse
# Standard libaries
# Custom libaries

logger = logging.getLogger('main')


def get_args(default):
    """
    This function gets the command line arguments and passes any unknown arguments to ALE.
    :param default: dictionary of default arguments with keys as `dest`
    :return: command line arguments
    """
    assert isinstance(default, dict), 'default_dict must be a dictionary of default arguments'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-g', '--game', dest='game', default=default.get('game', 'pong'), type=str, help="Name of game in ROM directory")
    parser.add_argument('-e', '--epochs', dest='epochs', default=default.get('epochs', 200), type=int, help="Number of Learning Epochs")
    parser.add_argument('-i', '--iter', dest='iter', default=default.get('iter', 500), type=int, help="Number of Iterations per Epoch")
    parser.add_argument('-d', '--display', dest='display', default=default.get('display', True), type=bool, help="Display Game while learning and testing")
    parser.add_argument('')





    return parser.parse_known_args(sys.argv)

if __name__ == '__main__':

