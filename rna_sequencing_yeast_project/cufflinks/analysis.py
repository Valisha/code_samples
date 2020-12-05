#!/usr/bin/env python3 
gene_list_salt = []
gene_list_sorb = []
with open("/home/shah.val/BINF6308/assmt11/cufflinks/exp_salt_out/gene_exp.diff","r") as f:
    lines = f.readlines()[1:]
    print(len(lines))
    for line in lines: 
        line = line.split('\t')
        #print(line)
        qvalue = float(line[12])
        logvalue =float(line[9])
        if qvalue < 0.01 and abs(logvalue) > 1:
            gene_list_salt.append(line[2])
with open("/home/shah.val/BINF6308/assmt11/cufflinks/exp_sorb_out/gene_exp.diff","r") as f:
    lines = f.readlines()[1:]
    print(len(lines))
    for line in lines: 
        line = line.split('\t')
        #print(line)
        qvalue = float(line[12])
        logvalue =float(line[9])
        if qvalue > 0.01 and abs(logvalue) > 1:
            gene_list_sorb.append(line[2])
lst3 = open("file1.txt","w")
def intersection(lst1,lst2):
    for value in lst1:
        if value in lst2:
            newstring = str(value)
            lst3.write(value+"\t")
    lst3.close()
lst1 = gene_list_salt
lst2 = gene_list_sorb
intersection(lst1,lst2)
