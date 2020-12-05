#!/usr/bin/env python3
"""
test file for my_io.py
"""
import os
import pytest

from assignment5 import my_io

FILE_TEST = "test.txt"


def test_existing_get_fh_4_reading():
    _create_test_file(FILE_TEST)
    test = my_io.get_fh(FILE_TEST, "r")
    assert hasattr(test, "readline")
    test.close()
    os.remove(FILE_TEST)


def test_existing_get_fh_4_writing():
    test = my_io.get_fh(FILE_TEST, "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_TEST)


def test_get_fh_4_IOError():
    with pytest.raises(IOError):
        my_io.get_fh("does_not_exist.txt", "r")


def test_mkdir_from_infile():
    file = 'test/test.txt'
    dir_ = os.path.dirname(file)
    my_io.mkdir_from_infile(file)
    assert os.path.exists(dir_) is True, "Not able to create a directory from 'test/test.txt'"
    os.rmdir(dir_)


def test_get_fh_4_TypeError():
    _create_test_file(FILE_TEST)
    with pytest.raises(TypeError):
        my_io.get_fh([],"r")
    os.remove(FILE_TEST)


def test_mkdir_from_directory_only():
    file = 'test/'
    dir_ = os.path.dirname(file)
    my_io.mkdir_from_infile(file)
    assert os.path.exists(dir_) is True, "Not able to create a directory from 'test'/"
    os.rmdir(dir_)


def test_mkdir_from_with_file_OSError():
    file = '/OUTPUT_CANT_BE_MADE_IN_ROOT/test.txt'
    with pytest.raises(OSError):
        my_io.mkdir_from_infile(file)


def test_mkdir_from_with_file_PermissionError():
    file = '/Users/username/test.txt'
    with pytest.raises(PermissionError):
        my_io.mkdir_from_infile(file)


def test_mkdir_from_with_file_FileNotFoundError():
    file = 'test.txt'
    with pytest.raises(FileNotFoundError):
        my_io.mkdir_from_infile(file)


def _create_test_file(file):
    open(file, 'w').close()
