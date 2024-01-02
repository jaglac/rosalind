# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:30:48 2024

@author: Caitlin Jagla

@title: Inferring mRNA from Protein (Rosalind Problem #10)
                                  
@url: https://rosalind.info/problems/mrna/
"""

from functools import reduce
from operator import mul

codon_freq = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2,
    'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    'STOP': 3
    }

def load_dna_file(fname):
    with open(fname) as inf:
        dna = inf.read()
    return "".join(dna.split())   # removes all whitespace

def num_rna_strings(dna, modulo=None):
    if modulo:
        reduce_fn = lambda a, b: (a * b) % modulo
    else:
        reduce_fn = mul
    freqs = (codon_freq[base] for base in dna)
    return reduce(reduce_fn, freqs, codon_freq["STOP"])

dna = load_dna_file("rosalind10.txt")
num = num_rna_strings(dna, 1000000)
print(num)
    