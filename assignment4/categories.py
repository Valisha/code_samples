#!/usr/bin/env python3
"""
Code to make the file\
 that counts the number of \
occurences of each and every description in the file
"""


def occurence_counter(chr_lines):
    """
    Function uses counter to count 'Category'
    """
    counter = dict(Counter(list(chr_lines['Category'])))
    return counter


def output_file(counter, file_category):
    """
    Creates the output file
    """
    out_file = open('OUTPUT/categories.txt', 'w')
    out_file.write('Category' +\
 '\t' + 'Occurence' +\
  '\t' + 'Description' + '\n')
    dict_category = {}
    for line in file_category:
        l_new = line.strip('\n').split('\t')
        dict_category.update({l_new[0]: l_new[1]})
    for key, val in counter.items():
        for key1, val1 in dict_category.items():
            if key == key1:
                out_file.write(str(key) + '\t' +\
 str(val) + '\t' + str(val1) + '\n')


if __name__ == "__main__":
    from collections import Counter
    from assignment4.my_io import open_file, save_as_dict
    import argparse
    PARSER = argparse.ArgumentParser(description="please\
enter the filename with the categories")
    PARSER.add_argument('--infile', '-i1', dest='filename1',\
help='Path to the gene description file to open', type=str)
    PARSER.add_argument('--infile2', '-i2',\
dest='file_category', help='Path to the gene category to open', type=str)
    ARGS = PARSER.parse_args()
    FILE1 = ARGS.filename1
    FILE_CATEGORY = ARGS.file_category
    FILE1 = open_file(FILE1)
    FILE_CATEGORY = open_file(FILE_CATEGORY)
    CHR_LINES = save_as_dict(FILE1)
    COUNTER = occurence_counter(CHR_LINES)
    output_file(COUNTER, FILE_CATEGORY)
