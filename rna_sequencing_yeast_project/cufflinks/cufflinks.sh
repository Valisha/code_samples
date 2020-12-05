#!/usr/bin/env bash 
for i in exp1 exp2 exp3 salt1 salt2 sorb1 sorb2;
do cufflinks ../bam/$i/$i.bam -G ../yeast/Saccharomyces_cerevisiae.R64-1-1.95.gtf -o $i -M ../yeast/mask.gtf --library-type=fr-firststrand 
done
