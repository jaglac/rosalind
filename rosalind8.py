# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 11:11:23 2024

@author: Caitlin Jagla

@title: Finding Longest Common Substring (Rosalind Problem #8)
                                  
@url: https://rosalind.info/problems/lcsm/
"""

# read dna sequences into list
dna = {}
with open("rosalind8.txt", "r") as data:
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
seqs = list(dna.values())    

# define function to find longest common substring
def lcsm(string_list):

    strands = sorted(string_list, key=len)
    shortest_strand = strands[0]
    longest_motif = ''

    for i in range(len(shortest_strand)):
        for j in range(i + len(longest_motif) + 1, len(shortest_strand) + 1):
            motif = shortest_strand[i:j]
            if all(motif in strand for strand in strands[1:]):
                longest_motif = motif

    return longest_motif

# run function and print result
string = lcsm(seqs)
print(string)

data.close()