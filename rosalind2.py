# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:22:46 2023

@author: Caitlin Jagla

@title: Transcribing DNA into RNA (Rosalind Problem #2)

@url: https://rosalind.info/problems/rna/
"""

f = open("rosalind2.txt", "r")

data = f.read()

data.replace("T", "U")

print(data.replace("T", "U"))

f.close()

