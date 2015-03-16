#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Will Brennan'

# built-in libarys
import os
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
    parser.add_argument('-g', '--game', dest='game', default=default.get('game', 'pong'), type=str, help="Name of game in ROM directory")
    parser.add_argument('-w', '--network', dest='network', default=default.get('network', ''), type=str, help='Filepath of network to run')
    parser.add_argument('-n', '--name', dest='name', default=default.get('name', ''), type=str, help='Name for IO')
    if args_string:
        args_string = args_string.split(' ')
        args = parser.parse_args(args_string)
    else:
        args = parser.parse_args()
    if not args.name:
        args.name = args.game+'-'+datetime.datetime.today().strftime("%d-%m-%Y")
    return args


def ale_run_wrapper(game=None, network=None):
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
    ale_run_wrapper(game=args.game, network=args.network)