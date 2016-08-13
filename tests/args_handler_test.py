# -*- coding: utf-8 -*-

import os 
import pytest
import datetime

from superdir.args_handler import output_dir_name, handle_args

def test_output_dir_name():

    dt_now = datetime.datetime.now()
    year, month, day, hour, minute = dt_now.year, dt_now.month, dt_now.day, dt_now.hour, dt_now.minute
    datestring = '{}-{}-{}-{}-{}'.format(year, month, day, hour, minute)

    assert output_dir_name(datestring=datestring) == '-'.join(['SUPERDIR_OUTPUT',datestring])
    assert output_dir_name(dir_suffix='TEST_SUFFIX', datestring=datestring) == '-'.join(['TEST_SUFFIX', datestring])

def test_handle_args_tty_no_args():

    assert False

def test_handle_args_tty_one_arg():

    assert False

def test_handle_args_tty_two_args():

    assert False

def test_handle_args_pipe_no_args():

    assert False

def test_handle_args_pipe_one_args():

    assert False





