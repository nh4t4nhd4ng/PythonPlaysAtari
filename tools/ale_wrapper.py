#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Will Brennan'

# built-in libarys
import os
import numpy
import logging
import subprocess
# Standard libaries
import cv2
# Custom libaries

logger = logging.getLogger('main')


class AleInterface(object):
    """

    """
    def __init__(self, display=True, skip=False, rom_path=None):
        self.display = display
        self.skip = skip
        logger.info('Initialising Ale Interface ')
        assert rom_path, 'No Atari ROM path or name passed.'
        if '.' not in rom_path:
            logger.debug('Rom name passed, generating path')
            base_path = ''.join(map(lambda i: i+'/', os.path.realpath(__file__).split('/')[:-2]))
            rom_path = '{0}roms/{1}.rom'.format(base_path, rom_path)
            logger.debug('Looking for rom in location {0}'.format(rom_path))
        assert os.path.exists(rom_path), 'rom_path, {0}, does not exist'.format(rom_path)
        logger.debug('{0} does exist'.format(rom_path))
        logger.info('Calling ALE via subprocess.Popen')
        command = './../libraries/ale/ale -max_num_episodes 0 -game_controller fifo_named -disable_colour_averaging true -run_length_encoding false -frame_skip '+str(self.skip_frames)+' -display_screen '+self.display_screen+self.game_ROM
        self.proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)
        logger.debug('ALE subprocess active.')
        logger.debug('Conducting further variable initialisation')
        # Setup of interface
        self.actions = []
        self.grey_screen = numpy.array(
            [[0, 136.0/4, 152.0/3, 52, 136.0/3, 7.066666666666667140e+01, 64, 5.066666666666666430e+01,
              136.0/3, 4.933333333333333570e+01, 136.0/3, 3.466666666666666430e+01,
              2.000000000000000000e+01, 2.533333333333333215e+01, 3.066666666666666785e+01, 36],
             [64, 72, 220.0/3, 76, 220.0/3, 96, 9.066666666666667140e+01, 7.733333333333332860e+01, 72, 76, 7.466666666666667140e+01, 64, 52, 5.733333333333333570e+01, 184.0/3, 6.533333333333332860e+01],
             [108, 100, 284.0/3, 100, 9.866666666666667140e+01, 1.186666666666666714e+02, 1.146666666666666714e+02, 1.026666666666666714e+02, 9.866666666666667140e+01, 1.026666666666666714e+02, 1.013333333333333286e+02, 9.333333333333332860e+01, 84, 8.666666666666667140e+01, 8.933333333333332860e+01, 284.0/3],
             [144, 124, 352.0/3, 1.226666666666666714e+02, 1.226666666666666714e+02, 1.400000000000000000e+02, 1.373333333333333428e+02, 128, 1.213333333333333286e+02, 1.266666666666666714e+02, 128, 1.213333333333333286e+02, 1.133333333333333286e+02, 1.133333333333333286e+02, 116, 120],
             [176, 144, 404.0/3, 1.426666666666666572e+02, 144, 160, 1.586666666666666572e+02, 1.480000000000000000e+02, 1.426666666666666572e+02, 148, 1.506666666666666572e+02, 144, 1.373333333333333428e+02, 1.386666666666666572e+02, 1.413333333333333428e+02, 1.426666666666666572e+02],
             [200, 496.0/3, 152, 1.613333333333333428e+02, 1.653333333333333428e+02, 1.773333333333333428e+02, 1.773333333333333428e+02, 1.693333333333333428e+02, 1.626666666666666572e+02, 1.666666666666666572e+02, 172, 168, 1.626666666666666572e+02, 1.613333333333333428e+02, 164, 1.653333333333333428e+02],
             [220, 556.0/3, 1682, 1.773333333333333428e+02, 556.0/3, 1.946666666666666572e+02, 196, 188, 1.813333333333333428e+02, 1.866666666666666572e+02, 1.933333333333333428e+02, 188, 556.0/3, 184, 184, 1.866666666666666572e+02],
             [236, 608.0/3, 556.0/3, 196, 204, 212, 2.133333333333333428e+02, 2.066666666666666572e+02, 200, 616.0/3, 2.133333333333333428e+02, 2.093333333333333428e+02, 2.066666666666666572e+02, 616.0/3, 616.0/3, 616.0/3]])
        # Game Variables
        self.next_image = []
        self.game_over = True
        self.current_points = 0
        logger.debug('Initialisation complete')

    def __del__(self):
        """

        :return:
        """
        logger.info('Winding up ALE interface')
        self.proc.stdin.close()
        self.proc.stdout.close()
        self.proc.stderr.close()
        logger.debug('Subprocess Pipes Closed')
        self.proc.kill()
        logger.debug('Subprocess killed :( ')

    def start_game(self):
        """

        :return:
        """
        pass

    def end_game(self):
        pass

    def interact(self, action):
        assert isinstance(action, int), 'Action must be an integer for list access'
        assert 0 <= action <= len(self.actions), 'Action must be between 0 and {0}'.format(len(self.actions))
        action = self.actions[action]
        out_string = "{0},{1}\n".format(action, numpy.random.randint(255))
        logger.debug('')
        self.proc.stdin.write(out_string)
        self.proc.stdin.flush()
        line_out = self.proc.stdout.readline()
        assert line_out.count(":") == 1, "line_out invalid - {0} colons found".format(line_out.count(":"))
        assert len(line_out) >= 2, "Invalid - Length of line is too small ({0} characters)".format(len(line_out))
        self.image_string, episode_info = line_out[:-2].split(":")
        assert episode_info.count(",") == 1, "Episode_info invalid - {0} commas found ".format(episode_info.count(","))
        episode_info = map(lambda i: int(i), episode_info.split(","))
        self.game_over = bool(episode_info[0])
        self.score = episode_info[2]
        image = self.process_frame(self.image_string)
        if self.display:
            cv2.imshow('Atari Emulator', image)
        return image

    def process_frame(self, image_string):
        assert isinstance(image_string, str), "image_string must be a string"
        arr = self.grey_screen
        # Crop irrelevant lines from beginning and end
        cropped = image_string[160*33*2:160*193*2]
        # Split cropped image string into a list of hex codes
        hexs = [cropped[i*2:i*2+2] for i in range(len(cropped)/2)]
        # Map each element of the list to the corresponding gray value
        grays = numpy.asarray(map(lambda hex_val: arr[int(hex_val[1], 16), int(hex_val[0], 16)], hexs))
        # Turn the array into an image object and downscale
        img = Image.fromarray(grays.reshape((160, 160)))
        new_size = self.desired_image_size, self.desired_image_size
        img.thumbnail(new_size, Image.NEAREST)
        # Get pixel data again
        norm_pixels = numpy.asarray(img, dtype=numpy.float32)/256.0
        return image, norm_pixels


if __name__ == '__main__':
    Ale = AleInterface(rom_path='breakout')
