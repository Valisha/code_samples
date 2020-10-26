#!/usr/bin/env bash 
# buildIndex.sh 

"""
Building index using Trinity fasta file and salmon indexing
"""


salmon index -t /scratch/SampleDataFiles/Trinity.fasta -i AipIndex k 25 
