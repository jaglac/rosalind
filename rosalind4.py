# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:38:53 2023

@author: Caitlin Jagla

@title: Computing GC Content (Rosalind Problem #4)

@url:https://rosalind.info/problems/gc/
"""

from collections import Counter

dna = {}

with open("rosalind4.txt", "r") as data:
    for line in data:
        line = line.strip()
        if ">" in line:
            seq_name = line[1:]
            if seq_name not in dna:
                dna[seq_name] = []
            continue
        dna[seq_name].append(line)

for seq_name in dna:
    dna[seq_name] = "".join(dna[seq_name])
    nucl_counts = Counter(dna[seq_name])
    gc = (nucl_counts["G"]+nucl_counts["C"])/float(len(dna[seq_name]))*100
    print(seq_name, "\n", gc)

