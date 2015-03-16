#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Will Brennan'

# built-in libarys
import os
import logging
import argparse
import cPickle as pickle
# Standard libaries
import numpy
import theano
# Custom libaries

logger = logging.getLogger('main')


class DeepQLearner(object):
    def __init__(self, args):
        logger.info('initialising DeepQLearner')
        assert isinstance(args, argparse.Namespace), 'args must be a '
        self.args = args
        logger.debug('Generating training domain')
        self.path = ''.join(map(lambda i: i+'/', os.path.abspath(__file__).split('/'))[:-1])[:-1]
        self.path = '{0}/data/{1}/'.format(self.path, args.name)
        self.layers = None
        logger.debug('initialisation complete')

    def train(self):
        num_batches_valid = states.shape[0] // self._batch_size
        self.states_shared.set_value(states)
        self.states_shared_next.set_value(next_states)
        self.actions_shared.set_value(actions)
        self.rewards_shared.set_value(rewards)
        for epoch in xrange(epochs):
            losses = []
            for b in xrange(num_batches_valid):
                loss = self._train(b)
                losses.append(loss)
            mean_train_loss = numpy.sqrt(numpy.mean(losses))
            return mean_train_loss

    def action(self):
        pass

    def save(self, pickle_name=''):
        logger.debug('Saving {0}'.format(pickle_name))
        path = self.check_pickle(pickle_name=pickle_name, saving=False)
        pickle.dump(self.layers, path)
        logger.debug('{0} has been saved to {1}'.format(pickle_name, path))

    def load(self, pickle_name=''):
        logger.debug('Loading {0}'.format(pickle_name))
        path = self.check_pickle(pickle_name=pickle_name, loading=True)
        temp_net = pickle.load(self.layers, path)
        logger.debug('{0} has been loaded from {1} to cache'.format(pickle_name, path))
        pass
        logger.debug('loaded from cache, loading complete')

    def check_pickle(self, pickle_name='', loading=False, saving=False):
        base = os.path.dirname(os.path.realpath(__file__))
        path = '{0}/data/{1}/{2}.pkl'.format(base, self.path, pickle_name)
        dirc = '{0}/data/{1}/'.format(base, self.path)
        assert loading != saving, 'loading and saving optional parameters must have opposite values'
        if loading:
            assert os.path.exists(path), '{0} does not exist'.format(path)
        if saving:
            assert os.path.isdir(dirc), 'specified diectory does not exist ({0})'.format(dirc)
            assert not os.path.exists(path), '{0} already exists, cannot overwrite'.format(path)
        return path