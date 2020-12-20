#!/usr/bin/env bash

read -p 'Path to VCF file: ' VCF

plink --vcf $VCF --double-id --allow-extra-chr --set-missing-var-ids @:# --make-bed --pca --out ouput_acs
