#!/usr/bin/env python3

import pytest
import sys

from pdb_fasta_splitter import (get_fh, get_header_and_sequence_lists, _check_size_of_lists)
def test_get_fh():
    with pytest.raises(ValueError):
        get_fh('ss.txt', 'w')
def test_file_path():
    with pytest.raises(IOError):        
        get_fh('ss1.txt', 'r')
def test__check_size_of_lists():
    fh_in = get_fh('ss.txt', 'r')
    header_list, seq_list = get_header_and_sequence_lists(fh_in)
    assert _check_size_of_lists(header_list, seq_list) == True
