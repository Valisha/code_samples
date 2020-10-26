#!/usr/bin/env bash
# renderMerge.sh 
"""
Script fo rendering the .Rmd file
"""
R -e "rmarkdown::render('mergeKo.Rmd',output_format='all')"
