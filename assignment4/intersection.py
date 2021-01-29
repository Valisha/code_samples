#!/usr/bin/env python3
"""
File to get the common genes in both the files
"""


def gene_list(file1, file2):
    """Creating the gene list
    """
    genes1 = []
    genes2 = []
    files1 = file1[1:]
    files2 = file2[1:]
    for line1, _ in enumerate(files1):
        lines1 = files1[line1].rstrip('\n').split('\t')
        genes1.append(lines1[0])
    for line2, _ in enumerate(files2):
        lines2 = files2[line2].rstrip('\n').split('\t')
        genes2.append(lines2[0])
    return genes1, genes2


def final_output(genes1, genes2):
    """
    Saving all the output
    """
    common_genes = []
    for line1, _ in enumerate(genes1):
        for line2, _ in enumerate(genes2):
            if genes1[line1] == genes2[line2]:
                common_genes.append(genes1[line1])
    not_list_chr21 = []
    for line1 in genes1:
        if line1 not in not_list_chr21:
            not_list_chr21.append(line1)
    not_list_hugo = []
    for line2 in genes2:
        if line2 not in not_list_hugo:
            not_list_hugo.append(line2)
    return common_genes, not_list_chr21, not_list_hugo


if __name__ == "__main__":
    from assignment4.my_io import open_file
    import argparse
    import sys
    OUT_FILE = open('OUTPUT/intersection_output.txt', 'w')
    PARSER = argparse.ArgumentParser(description="please enter the filename with the categories")
    PARSER.add_argument('--infile1', '-i1',\
dest='filename1', help='Path to the\
gene description file to open', type=str)
    PARSER.add_argument('--infile2', '-i2',\
dest='filename2', help='Path to the\
gene category to open', type=str)
    ARGS = PARSER.parse_args()
    F1 = ARGS.filename1
    F2 = ARGS.filename2
    FILE1 = open_file(F1)
    FILE2 = open_file(F2)
    GENES1, GENES2 = gene_list(FILE1, FILE2)
    COMMON_GENES, UNIQUE_VALUES_CHR21, UNIQUE_VALUES_HUGO = final_output(GENES1, GENES2)
    sys.stdout = open('OUTPUT/intersection_output.txt', 'w')
    print('Number of unique\
gene names in {0}: {1}'.format(F1, len(UNIQUE_VALUES_CHR21)))
    print('Number of unique gene\
names in {0}: {1}'.format(F2, len(UNIQUE_VALUES_HUGO)))
    print('Number of common\
gene symbols found: {}'.format(len(COMMON_GENES)))
    print('Output stored\
in OUTPUT/intersection_output.txt')
    sys.stdout.close()
