#!/usr/bin/env python3 
lines = []
orf1s = []
orf2s = [] 
with open("file1.txt","r") as f:
    for line in f:
        lines.append(line)
        word = line.split('\t')
        orf1s.append(word[0])
        orf2s.append(word[1])
def is_neighbor(orf1,orf2):
    if orf1[0:3]==orf2[0:3] and abs(int(orf1[3:6]) - int(orf2[3:6])) < 4 and orf1 != orf2:
        return True 
    else:
        return False 
output2 = open("file2.txt","w")
output3 = open("file3.txt","w")
cluster=[line[0]]
start1 = orf1s[0]
start2 = orf2s[0]
for i in range(len(lines)):
    if is_neighbor(orf1s[i],orf1s[i-1]) and is_neighbor(orf2s[i],orf2s[i-1]):
        #print(orf1s[i])
        cluster.append(lines[i])
        #print(orf2s[i]+ orf2s[i-1])
    else:
        if orf1s[i] == orf1s[i-1] or orf2s[i]==orf2s[i-1]:
            continue
        elif len(cluster) >=3:
            orfStrings = " ".join([str(ele) for ele in cluster])
            output2.write(orfStrings)
            end1 = orf1s[i-1]
            end2 = orf2s[i-1]
            cluster_len = str(len(cluster))
            out3_string =str(cluster_len +" ORFs "+ start1 +"-"+ end1 +" matches "+ start2 +"-"+ end2+"\n")
            output3.write(out3_string)
            cluster = [lines[i]]
        else:
            cluster = [lines[i]]
            start1 = orf1s[i]
            start2 = orf2s[i]
output2.close()
output3.close()
