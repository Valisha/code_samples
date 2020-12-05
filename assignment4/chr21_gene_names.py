#!/usr/bin/env python3
"""
To print the protein from the file
"""
def open_file(file_name):
    """
    To open the file of interest and save it as readlines()
    """
    try:
        chr1 = open(file_name, 'r')
        chr1 = chr1.readlines()
        return chr1
    except ValueError:
        raise ValueError


def save_as_dict(chr_read):
    """
    Saves the file as a dictionary
    """
    keys = [key for key in chr_read[0].strip('\n').split('\t')]
    chr_lines = {key: [None]*len(chr_read) for key in keys}
    for line, _ in enumerate(chr_read[1:]):
        lines = chr_read[line].rstrip('\n').split('\t')
        for i, _ in enumerate(lines):
            chr_lines[keys[i]][line] = lines[i]
    return chr_lines


def get_the_protein(prot, chr_lines):
    """
    Prints out the description of the entered protein name
    """
    stdout_fileno = sys.stdout
    chrs = []
    for key in range(len(chr_lines['Gene Symbol'])):
        if chr_lines['Gene Symbol'][key] == prot:
            stdout_fileno.write(chr_lines['Description'][key] + '\n')
            chrs.append(key)
    if len(chrs) == 0:
        sys.exit('Not valid gene name')


if __name__ == "__main__":
    import argparse
    import sys
    PARSER = argparse.ArgumentParser(description='enter the file with the protein and descriptions')
    PARSER.add_argument('--infile', '-i',\
dest='file_name', type=str,\
help='Path to the file to open')
    ARGS = PARSER.parse_args()
    INFILE = ARGS.file_name
    FH_IN = open_file(INFILE)
    CHR_LINES = save_as_dict(FH_IN)
    PROT = input(str("Enter gene name of interest. Type quit or exit: "))
    if PROT.lower() == 'quit':
        sys.exit("Thanks for querying the data")
    else:
        get_the_protein(PROT, CHR_LINES)

