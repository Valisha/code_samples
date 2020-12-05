#!/usr/bin/env python3
"""
File for get_gene_info.py
"""

def modify_host_name(host):
    """
    Modify the host name to get to the correct directory
    """
    host = host.lower()
    host_keywords = config.get_host_keywords()
    for key, val in host_keywords.items():
        if host == key:
            return val
    list_keywords = list(host_keywords.keys())
    if host not in list_keywords:
        _print_host_directories()


def _print_host_directories():
    sys.exit('Either the Host Name you are searching \
for is not in the database or \
If you are trying to use the \
scientific name please put \
the name in double quotes: "Scientific name"\nHere is \
a (non-case sensitive) list of available \
Hosts by scientific name\n1. Homo_sapiens\n2.\
 Bos_taurus\n3.\
 Equus_caballus\n4. Mus_musculus\n5. Ovis_aries\n6.\
 Rattus_norvegicus\nHere is a (non-case sensitive)\
 list of available Hosts by common name\n1. Bos taurus\n2.\
 Cow\n3. Cows\n4. Equus caballus\n5.\
 Homo sapiens\n6. Horse\n7. Horses\n8.\
 Human\n9. Humans\n10. Mice\n11. Mouse\n12.\
 Mus musculus\n13. Ovis aries\n14.\
 Rat\n15. Rats\n16. Rattus norvegicus\n17. Sheep')


def get_gene_data(file_name):
    """
    prints out the tissues from that gene name
    """
    file_read = file_name.readlines()
    for line in file_read:
        line.strip('\n')
        values = line.split('     ')
        if values[0] == 'EXPRESS':
            tissue_names = re.split(r'\|', values[1])
    return tissue_names


def main():
    """
    function to call all the functions and print out the correct output
    """
    parser = argparse.ArgumentParser(description="Please enter\
the host name and the gene name\
 to access the file of interest")
    parser.add_argument('-host', dest='host_name', help='Please enter the host name', type=str)
    parser.add_argument('-gene', dest='gene_name', help='Please enter the gene name', type=str)
    args = parser.parse_args()
    if not args.host_name:
        host = 'Homo Sapiens'
        gene = 'TGM1'
    else:
        host = args.host_name
        gene = args.gene_name
    filename = modify_host_name(host)
    file1 = "/".join((config.get_unigene_directory(),\
 filename, gene + "." + config.get_unigene_extension()))
    opened_file = my_io.get_fh(file1, 'r')
    if my_io.is_valid_gene_file_name(file1):
        print(f"\nFound Gene {gene} for {host}")
    else:
        print("Not Found")
        print(f"Gene {gene} does not exist for {host}. exiting now...", file=sys.stderr)
        sys.exit()
    tissue_names = get_gene_data(opened_file)
    print("In {0}, There are {1}\
 tissues that {2} is expressed in".format(host, \
len(tissue_names), gene))
    for t_index, _ in enumerate(tissue_names):
        print(f'{t_index+1:2.0f}. {tissue_names[t_index]}')


if __name__ == "__main__":
    import argparse
    import re
    import sys
    from assignment5 import my_io
    from assignment5 import config
    main()
