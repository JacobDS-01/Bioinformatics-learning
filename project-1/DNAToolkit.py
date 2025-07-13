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

# Find the reverse compliment of a DNA string
def reverseCompl(dna_seq):

    # define compliments
    compliments = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}

    # string comprehension to reverse contents
    reversed_tmp = list(dna_seq[::-1])
    
    # replace each base with compliment
    for i in range(len(reversed_tmp)):
        nuc = reversed_tmp[i]
        reversed_tmp[i] = compliments[nuc]

    return ''.join(reversed_tmp)



