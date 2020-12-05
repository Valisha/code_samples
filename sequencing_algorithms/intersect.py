#!/usr/bin/env python3 
fil1 = open("file1.bed","r")
fil2 = open("file2.bed","r")
filr1 = fil1.readlines()
filr2 = fil2.readlines()
start1s = []
start2s = []
end1s = []
end2s = []
chr1s = [] 
chr2s = []
for line in filr1:
    line = line.split('\t')
    start1 = line[1]
    end1 =line[2]
    start1s.append(start1)
    end1s.append(end1)
    chr1s.append(line[0])
    start1 = 0 
    end1 = 0 
for line in filr2:
    line = line.split('\t')
    start2 = line[1]
    end2 = line[2]
    start2s.append(start2)
    end2s.append(end2)
    chr2s.append(line[0])
    start2 = 0
    end2 = 0
start_news =[]
end_news = []
i = 0 
j = 0 
while i < len(chr1s) and j < len(chr2s):
    if chr1s[i]==chr2s[j]:
        if start1s[i] < start2s[j] < end1s[i] < end2s[j]:
            start_news.append(start2s[j])
            end_news.append(end1s[i])
        elif start1s[i] < start2s[j] < end2s[j] < end1s[i]:  
            start_news.append(start2s[j])
            end_news.append(end2s[j])
        elif start2s[j] < start1s[j] < end1s[j] < end2s[j]:
            start_news.append(start1s[i])
            end_news.append(end1s[i])
        elif start2s[j] < start1s[j] < end2s[j] < end1s[j]:
            start_news.append(start1s[i])
            end_news.append(end2s[j])
        j += 1
        i += 1 
    else :
            j += 1 
print(start_news) 
print(end_news)    
