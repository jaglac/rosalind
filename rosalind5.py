# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:04:30 2023

@author: Caitlin Jagla

@title: Counting Point Mutations (Rosalind Problem #5)
                                  
@url: https://rosalind.info/problems/hamm/
"""

def hamm_dist(dna1, dna2):
    """
    Calculates the Hamming distance between two strings of DNA.

    Parameters
    ----------
    dna1 : str
        First string of DNA.
    dna2 : str
        Second string of DNA.

    Returns
    -------
    The Hamming distance between the two strings of DNA.
    """
    if len(dna1) != len(dna2):
        raise ValueError("Strings must be of equal length")

    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance

f = open("rosalind5.txt", "r")
dna1 = f.readline()
dna2 = f.readline()

print(hamm_dist(dna1, dna2))

f.close()