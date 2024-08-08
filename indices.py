import sys
import re

def get_indices(pdb_file):
    disacc_file = pdb_file.split('/')[-1]
    adjacent_digits = re.findall(r'\d', disacc_file)
    digits = [int(num) for num in adjacent_digits]
   
    fst  = 1
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
            arr = line.split()
            #print(arr)
            #atom_index = int(line[6:11].strip())
            atom_index = int(arr[1])
            #atom_name = line[12:16].strip()
            atom_name = arr[2]
            #residue_number = int(line[22:26].strip())
            residue_number = int(arr[4])
            
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
