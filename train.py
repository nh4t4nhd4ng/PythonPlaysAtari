#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Will Brennan'

# built-in libarys
import os
import sys
import logging
import argparse
import datetime
# Standard libaries
import numpy
# Custom libaries
import DeepQ
import tools

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
    parser.add_argument('-g', '--game', dest='game', default=default.get('game', 'pong'), type=str, help="Name of game in ROM directory")
    parser.add_argument('-e', '--epochs', dest='epochs', default=default.get('epochs', 200), type=int, help="Number of Learning Epochs")
    parser.add_argument('-i', '--iter', dest='iter', default=default.get('iter', 500), type=int, help="Number of Iterations per Epoch")
    parser.add_argument('-d', '--display', dest='display', action="store_false", help="Display Game while learning and testing")
    parser.add_argument('-n', '--name', dest='name', default=default.get('name', ''), type=str, help='Name for IO')
    if args_string:
        args_string = args_string.split(' ')
        args = parser.parse_args(args_string)
    else:
        args = parser.parse_args()
    if not args.name:
        args.name = '{0}-{1}'.format(args.game, datetime.datetime.today().strftime("%d-%m-%Y-%H-%M"))
    return args


if __name__ == '__main__':
    args = get_args()
    logger.setLevel(logging.INFO)
    base = os.path.dirname(os.path.realpath(__file__))
    os.mkdir('{0}/data/{1}'.format(base, args.name))
    path = '{0}/data/{1}/train.log'.format(base, args.name)
    fh, ch = logging.FileHandler(path), logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
    for i in [fh, ch]:
        i.setLevel(logging.INFO)
        i.setFormatter(formatter)
        logger.addHandler(i)
    QLearner = DeepQ.DeepQLearner(args=args)
    logger.info('complete')

