from DNAToolkit import *
import random

rndDNAStr = ''.join([random.choice(Nucleotides)
                     for nuc in range(20)])

rosalindStr = ''

#print(rndDNAStr)
print(reverseCompl(rosalindStr))