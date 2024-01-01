# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:04:30 2023

@author: Caitlin Jagla

@title: Translating RNA into Protein (Rosalind Problem #6)
                                  
@url: https://rosalind.info/problems/prot/
"""

rna_codons = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}


def translate_rna(rna):
    """Translates an RNA sequence into a protein sequence."""

    protein = ""
    for i in range(0, len(rna), 3):  # Iterate through codons
        codon = rna[i:i+3]
        amino_acid = rna_codons.get(codon, "")  # Get amino acid or empty string if unknown codon
        if amino_acid == "Stop":
            break  # Stop translation at stop codon
        protein += amino_acid
    return protein


f = open("rosalind6.txt", "r")
rna_sequence = f.readline()

protein_sequence = translate_rna(rna_sequence)

print(protein_sequence)

f.close()