# DNA Toolkit.py file
# This module provides basic functionalities for DNA sequence manipulation.

Nucleotides = ['A', 'C', 'G', 'T']

# Validate the given sequence is a DNA sequence
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq
        
# Count the frequency of each of the nucleotides in a sequence
def countNucFrequency(seq):
    tmpFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

# Replace T with U in DNA sequence to transcribe to RNA up to first 1000 chars in str
def transcribeRNA(dna_seq):
    return dna_seq.replace('T', 'U', 1000)