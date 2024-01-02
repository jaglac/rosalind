# -*- coding: Ttf-8 -*-
"""
Created on Tue Jan  2 15:45:47 2024

@author: Caitlin Jagla

@title: Open Reading Frames (Rosalind Problem #11)
                                  
@url: https://rosalind.info/problems/orf/
"""

def translate(codon):
    codon_table = {
        'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
        'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
        'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
        'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
        'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
        'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
        'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
        'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
        'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
        'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
        'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
        'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
        'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
        'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
        'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
        'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
    }
    if len(codon) == 3 and codon in codon_table:
        return codon_table[codon]

def rev_comp(dna_seq):
    nucleotides = { 'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    rev = reversed(dna_seq)
    return ''.join(nucleotides[base] for base in rev)

def get_orfs(dna_seq):
    orfs = []
    starts = []
    #scan for start codons
    for i in range(len(dna_seq)):
        aa = translate(dna_seq[i:i+3])
        if aa and aa == 'M':
            starts.append(i)
    #translate all codons in ORF until stop codon found
    for s in starts:
        prot_seq = ''
        stop = False
        for i in range(s, len(dna_seq), 3):
            aa = translate(dna_seq[i:i+3])
            if not aa:
                break
            if aa == 'Stop':
                stop = True
                break
            prot_seq += aa
        if stop:
            orfs.append(prot_seq)
    return(orfs)   

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

dna_dict = read_fasta_to_dict("rosalind11.txt")
dna_seq = list(dna_dict.values())[0]

print("\n".join(set(get_orfs(dna_seq) + get_orfs(rev_comp(dna_seq)))))