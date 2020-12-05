#!/usr/bin/env bash 
for i in exp1 exp2 exp3 salt1 salt2 sorb1 sorb2; 
do java -jar /usr/local/programs/Trimmomatic-0.36/trimmomatic-0.36.jar SE -threads 8 -phred33 /scratch/BINF6308_2019S/rnaseq/$i.fastq /home/shah.val/BINF6308/assmt11/trimmed/$i.fastq LEADING:25 TRAILING:25 SLIDINGWINDOW:3:25 MINLEN:50
wc -l /scratch/BINF6308_2019S/rnaseq/$i.fastq /home/shah.val/BINF6308/assmt11/trimmed/$i.fastq
done
