# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:23:36 2024

@author: Caitlin Jagla

@title: Overlap Graphs (Rosalind Problem #12)
                                  
@url: https://rosalind.info/problems/grph/
"""

def read_fasta_to_dict(filepath):
    with open(filepath, "r") as data:
        dna = {}
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
        data.close()
        return dna


    


