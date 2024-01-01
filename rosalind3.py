# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:25:19 2023

@author: Caitlin Jagla

@title: Complementing a Strand of DNA (Rosalind Problem #3)
                                       
@url: https://rosalind.info/problems/revc/
"""

from Bio.Seq import Seq

f = open("rosalind3.txt", "r")

seq = Seq(f.read())

print(seq.reverse_complement())

f.close()