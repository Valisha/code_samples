#!/usr/bin/env bash
R -e "rmarkdown::render('citeExample.Rmd', output_format='md_document')"
