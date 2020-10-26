#!/usr/bin/env bash 
# alignAll.sh 

"""
Script for aligining all the fastq file. bash scripting for looping over all the files and aligning each file. 
"""

outDir="quant/" # output directory
fastqPath="/scratch/SampleDataFiles/Paired/"
leftSuffix=".R1.paired.fastq"
rightSuffix=".R2.paired.fastq"
for leftInFile in $fastqPath*$leftSuffix
do
    pathRemoved="${leftInFile/$fastqPath/}"
    sampleName="${pathRemoved/$leftSuffix/}"
    echo $sampleName
    function align {
        salmon quant -l IU is \
            -1 /scratch/SampleDataFiles/Paired/$sampleName.R1.paired.fastq \
            -2 /scratch/SampleDataFiles/Paired/$sampleName.R2.paired.fastq \
            -i AipIndex \
            --validateMappings \
            -o $outDir$sampleName
    }
    align 1>align.log 2>align.err &  	
done
