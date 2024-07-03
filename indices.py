import sys
import re

def get_indices(pdb_file):
    adjacent_digits = re.findall(r'\d', pdb_file)
    digits = [int(num) for num in adjacent_digits]
    fst  = digits[0]
    snd = digits[1]

    phi_criteria = [
        f"resid 2 and name H{fst}",
        f"resid 2 and name C{fst}",
        f"resid 1 and name O{snd}",
        f"resid 1 and name C{snd}"
    ]
    
    psi_criteria = [
        f"resid 2 and name C{fst}",
        f"resid 1 and name O{snd}",
        f"resid 1 and name C{snd}",
        f"resid 1 and name H{snd}"
    ]
    
    with open(pdb_file) as f:
        data = f.readlines()
        
    phi_indices = [None] * len(phi_criteria)
    psi_indices = [None] * len(psi_criteria)

    for line in data:
        if line.startswith('ATOM'):
            atom_index = int(line[6:11].strip())
            atom_name = line[12:16].strip()
            residue_number = int(line[22:26].strip())
            
            atom_desc = f"resid {residue_number} and name {atom_name}"
            
            if atom_desc in phi_criteria:
                index = phi_criteria.index(atom_desc)
                phi_indices[index] = atom_index - 1
            if atom_desc in psi_criteria:
                index = psi_criteria.index(atom_desc)
                psi_indices[index] = atom_index - 1

    return [phi_indices, psi_indices]

if __name__ == "__main__":
    filename = sys.argv[1]
    indices = get_indices(filename)
    phi_indices = indices[0]
    psi_indices = indices[1]
    print(indices)
    #print(phi_indices)
    #print(psi_indices)
