#!/usr/bin/env python3 

with open("file1x.txt","r") as f:
    output = open("file1.txt", "w")
    #fr = [lines.split('\t') for lines in f.readlines()]
    for line in f: 
        queries = line.split('\t')
        qseqid = queries[0]
        sseqid = queries[1]
        if qseqid != sseqid: 
            output.write(line)
    
output.close()


# # blastp -query yeast_proteins.fasta -db yeastprots -out file1x.txt -evalue 1.0e-4 -outfmt 6 
