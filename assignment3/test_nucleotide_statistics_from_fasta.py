#!/usr/bin/env python3
"""
Test suite for nucleotide_statistics_from_fasta.py
"""
import pytest
from nucleotide_statistics_from_fasta import (get_fh, get_header_and_sequence_lists, _check_size_of_lists, _get_accession, _get_nt_occurence, print_sequence_stats)
file1 = 'influenza.fasta'
fh_in = open(file1, 'r')
header_list, seq_list = get_header_and_sequence_lists(fh_in)
f_out = open('out2.txt', 'w')
def test__get_accession():
    assert _get_accession(header_list[0]) == 'EU521893'
test__get_accession()
def test__get_nt_occurence():
    assert _get_nt_occurence('A', seq_list[0]) == 350
def test_print_sequence_stats():
    header = header_list[3:]
    with pytest.raises(SystemExit):
        print_sequence_stats(header, seq_list, f_out)
