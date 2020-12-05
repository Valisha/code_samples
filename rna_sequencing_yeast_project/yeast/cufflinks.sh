#!/usr/bin/env bash 
for i in exp1 exp2 exp3 salt1 salt2 sorb1 sorb2;
do cufflinks /home/shah.val/BINF6308/assmt11/bam/$i/$i.bam -o /home/shah.val/BINF6308/assmt11/gtf/$i -M mask.gtf -G Saccharomyces_cerevisiae.R64-1-1.95.gtf --library-type=fr-firststrand
done  
