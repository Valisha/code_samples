#!/usr/bin/env python3

import pytest
from assignment4.my_io import open_file, save_as_dict, get_the_protein

def test_open_file():
    with pytest.raises(ValueError):
        open_file('../../../chr2_genes.txt')

def test_save_as_dict():
    chr_read = open_file('/home/shah.val/programming6200/assignment4/chr21_genes.txt')
    chr_lines = save_as_dict(chr_read)
    assert len(chr_read) == len(chr_lines['Gene Symbol'])


def test_get_the_protein():
    chr_read = open('/home/shah.val/programming6200/assignment4/chr21_genes.txt')
    chr_lines = save_as_dict(chr_read)
    prot = 'TGTBDTK'
    with pytest.raises(SystemExit):
        get_the_protein(prot, chr_lines)

def test_get_the_prot_quit():
    chr_read = open('/home/shah.val/programming6200/assignment4/chr21_genes.txt')
    chr_lines = save_as_dict(chr_read)
    prot = 'quit'
    with pytest.raises(SystemExit):
         get_the_protein(prot, chr_lines)
