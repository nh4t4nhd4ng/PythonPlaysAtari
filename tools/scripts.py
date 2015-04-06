#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Will Brennan'

# built-in libarys
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
    parser.add_argument('-e', '--epochs', dest='epochs', default=default.get('epochs', 200), type=int, help="Number of Learning Epochs")
    parser.add_argument('-i', '--iter', dest='iter', default=default.get('iter', 500), type=int, help="Number of Iterations per Epoch")
    parser.add_argument('-d', '--display', dest='display', action="store_false", help="Display Game while learning and testing")
    parser.add_argument('-b', '--debug', dest='debug', action='store_false', help='Enable debugging logging')
    parser.add_argument('-n', '--name', dest='name', default=default.get('name', ''), type=str, help='Name for IO')
    if args_string:
        args_string = args_string.split(' ')
        args = parser.parse_args(args_string)
    else:
        args = parser.parse_args()
    if not args.name:
        args.name = '{0}-{1}'.format(args.game, datetime.datetime.today().strftime("%d-%m-%Y-%H-%M"))
    return args


def get_logger(level=logging.INFO, quite=False, debug=False, to_file=''):
    """
    This function initialises a logger to stdout.
    :return: logger
    """
    assert level in [logging.DEBUG, logging.INFO, logging.WARNING, logging.CRITICAL]
    logger = logging.getLogger('main')
    formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
    if debug:
        level = logging.DEBUG
    logger.setLevel(level=level)
    if not quite:
        if to_file:
            fh = logging.FileHandler(to_file)
            fh.setLevel(level=level)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        else:
            ch = logging.StreamHandler()
            ch.setLevel(level=level)
            ch.setFormatter(formatter)
            logger.addHandler(ch)
    return logger

