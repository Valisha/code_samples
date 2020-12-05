#!/usr/bin/env python3
"""Script that takes in a fasta file and outputs its statistics as tab separated file"""

import argparse
import re
import sys


def get_fh(file_to_open, mode):

    """function to open the file"""

    if mode not in ['r', 'r+']:
        raise ValueError
    try:
        fh_in = open(file_to_open, mode)
        return fh_in
    except IOError:
        raise IOError


def get_header_and_sequence_lists(fh_in):

    """Function to create two lists\
 from an input separating the header\
 based on occurence of '>' and returning\
 two lists of headers and sequences if\
 the length of these lists are the same"""

    headers = []
    seqs = []
    new_lines = []
    text = fh_in.readlines()
    for i, _ in enumerate(text):
        if text[i] != '':
            text_line = text[i].strip('\n')
            text_line_new = text_line.strip('')
            new_lines.append(text_line_new)
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

    """Check if the sizes of the headers and sequences lists is the same"""

    if len(header_list) == len(seq_list):
        return True
    if len(header_list) != len(seq_list):
        return False


def _get_accession(header):

    """get the accession number of the sequence from the fasta file"""

    head = header.split(' ')
    head1 = head[0]
    return head1


def _get_nt_occurence(nts, seq):

    """ Calculating the number of nucleotides\
 as given in the input. To be finally\
 used in print_sequence_stats function"""

    nt_occurence = len(re.findall(nts, seq))
    return nt_occurence


def print_sequence_stats(header_list, seq_list, f_out):

    """Function to calculate the statistics of the\
 sequences calculated. Takes in headers list,\
 sequences list and the output file as\
 input and outputs a tab separated file\
 with the accession number and stats of that sequence"""

    fh_out = open(f_out, 'w')
    str1 = ["Number", '\t', "Accession",\
 '\t', "A's", '\t', "G's", '\t', "C's", '\t', "T's",\
 '\t', "N's", '\t', "Length", '\t', "GC%"]
    str2 = ''.join(map(str, str1))
    fh_out.write(str2 + '\n')
    for i, _ in enumerate(header_list):
        num_as = _get_nt_occurence('A', seq_list[i])
        num_cs = _get_nt_occurence('C', seq_list[i])
        num_gs = _get_nt_occurence('G', seq_list[i])
        num_ts = _get_nt_occurence('T', seq_list[i])
        num_ns = _get_nt_occurence('N', seq_list[i])
        num_nts = [num_as, num_cs, num_gs, num_ts, num_ns]
        sum_nts = sum(num_nts)
        if sum_nts != len(seq_list[i]):
            sys.exit('Did not code this condition')
        length = len(seq_list[i])
        gc_perc = round((((num_gs+num_cs)/length)*100), 1)
        accession_string = _get_accession(header_list[i])
        str1 = [i, '\t', accession_string, '\t',\
 num_as, '\t', num_gs, '\t', num_cs, '\t', num_ts,\
 '\t', num_ns, '\t', length, '\t', gc_perc]
        str2 = ''.join(map(str, str1))
        fh_out.write(str2 + '\n')
        str1 = ''
    fh_out.close()
    return fh_out


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='file to be split')
    PARSER.add_argument('--infile', '-i', dest='filename',\
 type=str, help='Give the fasta sequence filename to do the splitting',\
 required=True)
    PARSER.add_argument('--outfile', '-o', dest='outfile',\
 type=str, help='Give the file for statistics output', required=True)
    ARGS = PARSER.parse_args()
    INFILE = ARGS.filename
    FH_IN = get_fh(INFILE, 'r')
    OUTFILE = ARGS.outfile
    HEADER, SEQ = get_header_and_sequence_lists(FH_IN)

    print_sequence_stats(HEADER, SEQ, OUTFILE)
    FH_IN.close()
