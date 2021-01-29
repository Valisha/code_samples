#!/usr/bin/env python3
"""
Sript to split a fasta file into headers and sequences.
"""

import argparse
import re
import sys


def get_fh(file_to_open, mode):

    """function to open the fasta file,\
takes the file to be opened and the mode of opening it as an input"""

    if mode not in ['r+', 'r']:
        raise ValueError
    try:
        fh_file = open(file_to_open, mode)
        return fh_file
    except IOError:
        raise IOError


def get_header_and_sequence_lists(fh_in):

    """function to split the the header and\
sequences into two difference lists,\
take the opened file as an input and returns two\
lists if the length of these lists are the same"""

    headers = []
    seqs = []
    text = fh_in.readlines()
    new_lines = []
    for i, _ in enumerate(text):
        if text[i] != '':
            t_val = text[i].strip('\n')
            t_new = t_val.strip('')
            new_lines.append(t_new)
    seq = ''
    for line, _ in enumerate(new_lines):
        if re.match(">", new_lines[line]):
            if len(seq) != 0:
                seqs.append(seq)
                seq = ''
            item = new_lines[line].split('>')
            item = ''.join(item)
            headers.append(item)
        else:
            item = str(new_lines[line])
            seq += item
    if len(seq) != 0:
        seqs.append(seq)
    if _check_size_of_lists(headers, seqs) is True:
        return headers, seqs
    if _check_size_of_lists(headers, seqs) is False:
        sys.exit("The length of the headers\
 list and sequences list did not match, please enter a valid file")


def _check_size_of_lists(header_list, seq_list):

    """function to check if the length of the header list and sequence list the same
    if not the program exits
    """

    if len(header_list) == len(seq_list):
        return True
    if len(header_list) != len(seq_list):
        return False

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='file to be split')
    PARSER.add_argument('--infile', '-i', dest='filename',\
 type=str, help='Give the fasta sequence filename to do the splitting', required=True)
    ARGS = PARSER.parse_args()
    INFILE = ARGS.filename
    FH_IN = get_fh(INFILE, 'r+')
    HEADER, SEQ = get_header_and_sequence_lists(FH_IN)
    FH_OUT = open('pdb_protein.fasta', 'w')
    SEQ = map(lambda x: x + '\n', SEQ)
    FH_OUT.writelines(SEQ)
    FH_OUT.close()
    FH_OUT_SS = open('pdb_ss.fasta', 'w')
    HEADER = map(lambda x: x + '\n', HEADER)
    FH_OUT_SS.writelines(HEADER)
    FH_OUT_SS.close()
