#!/usr/bin/env python3
seq = open("myseq.fq","r")
seqr = seq.readlines()
nts = []
import numpy
for line in range(1,len(seqr),4):
    seqr[line] = seqr[line].rstrip('\n')
    new_seq = list(seqr[line])
    nts.append(new_seq)
ntsa = []
col = []
for j in range(len(nts[0])):
    for i in range(len(nts)):
        nt = nts[i][j]
        col.append(nt)
    ntsa.append(col)
    col = []
def phred(qual):
    pred = ord(qual)-33
    return pred
values = []
for i in range(3,len(seqr),4):
    seqr[i] = seqr[i].rstrip('\n')
    values.append(seqr[i])
final_list = []
arr_vals = []
for i in range(len(values)):
    for j in range(len(values[i])):
            qual = values[i][j]
            final_val = phred(qual)
            final_list.append(final_val)
    arr_vals.append(final_list)
    final_list = []
cols = []
col1 = []
for j in range(len(arr_vals[0])):
    for i in range(len(arr_vals)):
        col1.append(arr_vals[i][j])
    cols.append(col1)
    col1 = []
list1 = []
colss = list(cols)
for i in range(1,len(ntsa)+1):
    list1.append(i)
print(list1)
import matplotlib.pyplot as plt
import tkinter
plt.boxplot(colss)
plt.show 
filename = "myplot.png"
plt.savefig(filename)
plt.close()
