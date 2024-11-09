def open_file(path):
    with open(path, "r") as f:
        return f.read()
    
def read_txt(file):
    return file.split(">")[1:]

def calculate_gc(sequence):
    gc_count = sum(1 for n in sequence if n in ['C', 'G'])
    return (gc_count / len(sequence)) * 100 if len(sequence) > 0 else 0 
    
def absolute_error(path):
    s = read_txt(path)
    
    gc = -1
    id_gc = ""
    
    for entry in s:
        parts = entry.splitlines()
        id_sequence = parts[0].strip() 
        
        sequence_dna = ''.join(parts[1:]).strip()  
        
        gc_cont = calculate_gc(sequence_dna)
        
        if gc_cont > gc:
            gc = gc_cont
            id_gc = id_sequence
    
    print(f"{id_gc}\n{gc:.6f}")

path = "src/GC/rosalind_gc.txt"
absolute_error(open_file(path))