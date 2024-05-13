# Fungi_3DGenome

## split_chromosomes.py

This script takes the input N x N hic matrix file of the genome in .txt format. In the array format, the script also takes the lengths of each chromosome present in the genome. Based on these lengths, this script splits the whole data into the individual matrices for each chromosome. The output files would be the individual matrices for each chromosome. 

## tuples_format.m

This MATLAB script takes the individual matrix generated from above script and converts them into the 3 column tuple format that is readable by other genome visualization tools. The input would be N x N matrix of a chromosome and the output would be the three tuple format of the chromosome. 
