#!/usr/boin/env python3

def open_file(file_name):
    """
    To open the file of interest and save it as readlines()
    """
    chr1 = open(file_name, 'r')
    chr1 = chr1.readlines()
    return chr1[1:]


def save_as_dict(chr_read):
    """
    Saves the file as a dictionary
    """
    keys = ['Gene Symbol', 'Description', 'Category']
    chr_lines = {key: [None]*len(chr_read) for key in keys}
    for line, _ in enumerate(chr_read):
        l = chr_read[line].rstrip('\n')
        l = l.split('\t')
        chr_lines['Gene Symbol'][line] =  l[0]
        chr_lines['Description'][line] = l[1]
        chr_lines['Category'][line] = l[2]
    return chr_lines


def get_unique_values(list1):
    not_list = []
    for i in list1:
        if i not in not_list and len(i) != 0:
            not_list.append(i)
    return not_list


def description_for_subcategories(not_list):
    cat_desc_dict = {}
    for cat in not_list:
        if cat == '1.1':
            cat_desc_dict.update({cat: 'Genes with 100% identity over a complete cDNA with defined functional association (for example, transcription factor, kinase).'})
        if cat == '1.2':
            cat_desc_dict.update({cat: 'Genes with 100% identity over a complete cDNA corresponding to a gene of unknown function (for example, some of the KIAA series of large cDNAs).'})
        if cat == '2.1':
            cat_desc_dict.update({cat: 'Genes showing similarity or homology to a characterized cDNA from any organism (25–100% amino-acid identity). This class defines new members of human gene families, as well as new human homologues or orthologues of genes from yeast, Caenorhabditis elegans, Drosophila, mouse and so on.'})
        if cat == '2.2':
            cat_desc_dict.update({cat: 'Genes with similarity to a putative ORF predicted in silico from the genomic sequence of any organism but which currently lacks experimental verification.'})
        if cat == '3.1':
            cat_desc_dict.update({cat: 'Genes with amino-acid similarity confined to a protein region specifying a functional domain (for example, zinc fingers, immunoglobulin domains).'})
        if cat == '3.2':
            cat_desc_dict.update({cat: 'Genes with amino-acid similarity confined to regions of a known protein without known functional association.'})
        if cat == '4.1':
            cat_desc_dict.update({cat: 'Predicted genes composed of a pattern of two or more consistent exons (located within <20 kb) and supported by spliced EST match(es).'})
        if cat == '4.2':
            cat_desc_dict.update({cat: 'Predicted genes corresponding to spliced EST(s) but which failed to be recognized by exon prediction programs.'})
        if cat == '4.3':
            cat_desc_dict.update({cat: 'Predicted genes composed only of a pattern of consistent exons without any matches to ETS(s) or cDNA. Intuitively, predicted genes from subcategory 4.1 are considered to have stronger coding potential than those of subcategory 4.3.'})
        if cat == '5':
            cat_desc_dict.update({cat: 'Pseudogenes may be regarded as gene-derived DNA sequences that are no longer capable of being expressed as protein products. They were defined as predicted polypeptides with strong similarity to a known gene, but showing at least one of the following features: lack of introns when the source gene is known to have an intron/exon structure, occurence of in-frame stop codons, insertions and/or deletions that disrupt the ORF or truncated matches. Generally, this was an unambiguous classification.'}) 
    return cat_desc_dict


def save_dict_file(cat_desc_dict):
    chr21_genes = open('chr21_genes_categories.txt','w')
    for key, val in cat_desc_dict.items():
        chr21_genes.write(key + '\t' + val + '\n')
    chr21_genes.close()
    return chr21_genes


if __name__ == "__main__":
    import argparse
    import sys
    from collections import OrderedDict
    PARSER = argparse.ArgumentParser(description='enter the file with the protein and descriptions')
    PARSER.add_argument('--infile', '-i', dest='file_name', type=str, help='Path to the file to open')
    ARGS = PARSER.parse_args()
    INFILE = ARGS.file_name
    FH_IN = open_file(INFILE)
    CHR_LINES = save_as_dict(FH_IN)
    UNIQUE_CATEGORIES = get_unique_values(CHR_LINES['Category'])
    DESCRIPTION_DICT = description_for_subcategories(UNIQUE_CATEGORIES)
    DESCRIPTION_DICT = dict(OrderedDict(sorted(DESCRIPTION_DICT.items())))
    save_dict_file(DESCRIPTION_DICT)
