# Problem
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'. Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

# Given
# A DNA string t having length at most 1000 nt.

# Return
# The transcribed RNA string of t.

def open_file(file):
    with open(file, "r") as f:
        s = f.read()
        
    return s 

def change_caracter(path):
    s = open_file(path)
    
    s = "".join(["U" if l == "T" else l for l in s])
    
    print(s)
    
path = "src/RNA/rosalind_rna.txt"
change_caracter(path)