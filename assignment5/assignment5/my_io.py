#!/usr/bin/env python3
"""
Script for my_io.py
"""
import os
from assignment5 import config


def get_fh(file, args):
    """
    Function to open the file. Calling the error strings from my_io.py to print out the correct error messages
    """
    try:
        fobj = open(file, args)
        return fobj
    except IOError as err:
        config.get_error_string_4_unable_to_open(file, args)
        raise err
    except ValueError as err:
        config.get_error_string_4_unable_to_open(file, args)
        raise err
    except TypeError as err:
        config.get_error_string_4_unable_to_open(file, args)
        raise err

def mkdir_from_infile(file):
    try:
        if not os.path.exists(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
    except PermissionError as err:
        config.get_error_string_4_unable_to_open(file, "r")
        raise err
    except FileNotFoundError as err:
        config.get_error_string_4_unable_to_open(file, )
        raise err
    except OSError as err:
        config.get_error_string_4_unable_to_open(file)
        raise err

def is_valid_gene_file_name(file1):
    isExist = os.path.exists(file1)
    return isExist

