# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:04:30 2023

@author: Caitlin Jagla

@title: Finding a Motif in DNA (Rosalind Problem #7)
                                  
@url: https://rosalind.info/problems/subs/
"""

def find_motif(s, t):
    loc=[]
    for i in range(len(s)):
        if s[i:].startswith(t):
            loc.append(i+1)
    return loc
        

f = open("rosalind7.txt", "r")
s = f.readline().strip()
t = f.readline().strip()

locs = find_motif(s, t)

print(*locs)

f.close()