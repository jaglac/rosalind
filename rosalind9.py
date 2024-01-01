# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 11:53:47 2024

@author: Caitlin Jagla

@title: Finding a Protein Motif (Rosalind Problem #9)
                                  
@url: https://rosalind.info/problems/mprt/
"""
import requests as r
from Bio import SeqIO
from io import StringIO
import re

# read uniprot ids in from file
ids = {}
with open("rosalind9.txt", "r") as data:
    for line in data:
        prot_id = line.strip().split("_",1)[0] # necessary to split based on underscore because long-format ids don't work in uniprot url
        ids[prot_id] = line.strip()

# fetch protein sequences from uniprot and store in dictionary
baseUrl="http://www.uniprot.org/uniprot/"
seqs = {}
for prot in list(ids.keys()):
    currentUrl=baseUrl+prot+".fasta"
    response = r.post(currentUrl)
    cData=''.join(response.text)
    Seq=StringIO(cData)
    pSeq=list(SeqIO.parse(Seq,'fasta'))
    if len(pSeq) > 0: # necessary because some protein IDs do not exist in uniprot and therefore return no sequence record
        seqs[prot] = str(pSeq[0].seq)


# search protein sequences for motif
motif = "(?=N[^P][ST][^P])"
pattern = re.compile(motif)
for prot in seqs:
    matches = pattern.finditer(seqs[prot])
    locs = []
    for match in matches:
        locs.append(match.start()+1)
    if len(locs) > 0:
        print(ids[prot])
        print(*locs)
    

    
data.close()    