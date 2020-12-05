#!/usr/bin/env bash 
for i in exp1 exp2 exp3 salt1 salt2 sorb1 sorb2; do  hisat2 -x /home/shah.val/BINF6308/assmt11/yeast/yeastindex -U $i.fastq --known-splicesite-infile /home/shah.val/BINF6308/assmt11/yeast/yeast_ss.txt --score-min L,-0.6,-0.6 | samtools sort -o /home/shah.val/BINF6308/assmt11/bam/$i/$i.bam
done
