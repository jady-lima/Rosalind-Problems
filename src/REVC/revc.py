# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given
# A DNA string s of length at most 1000 bp.

# Return
# The reverse complement s^c of s.

def open_file(path):
    with open(path, "r") as f:
        return f.read()

def complement(file):
    s = list(file)
    for i, l in enumerate(s):
        if (l == "A"):
            s[i] = "T"
        elif (l == "T"):
            s[i] = "A"
        elif (l == "C"):
            s[i] = "G"
        elif (l == "G"):
            s[i] = "C"
    s.reverse()
    print("".join(s))
    
path = "src/REVC/rosalind_revc.txt"
complement(open_file(path))