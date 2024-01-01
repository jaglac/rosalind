# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 17:43:56 2023

@author: Caitlin Jagla

@title: Counting DNA Nucleotides (Rosalind Problem #1) 

@url: https://rosalind.info/problems/dna/
"""

f = open("rosalind1.txt", "r")

data = f.read()

counts = [data.count("A"), data.count("C"), data.count("G"), data.count("T")]

print(*counts)

f.close()

