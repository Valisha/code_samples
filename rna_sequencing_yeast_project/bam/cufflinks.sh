#!/usr/bin/env bash 
for i in exp1 exp2 exp3 salt1 salt2 sorb1 sorb2;
do cufflinks -o $i --library0type fr-firstrand -g ../yeast/Saccharomyces_cerevisiae.R64-1-1.95.gtf -M ../yeast/mask.gtf ../bam/$1/$i.bam
done
