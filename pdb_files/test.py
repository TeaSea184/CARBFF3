import re

def get_linkages(pdb_file):
    # Extract digits from pdb file name
    adjacent_digits = re.findall(r'\d', pdb_file)
    digits = [int(num) for num in adjacent_digits]
    fst = digits[0]
    snd = digits[1]
    
    # Define the criteria for phi and psi atoms in the desired order
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
    
    # Read the PDB file
    with open(pdb_file) as f:
        data = f.readlines()
    f.close()
    # Initialize the indices lists with None
    phi_indices = [None] * len(phi_criteria)
    psi_indices = [None] * len(psi_criteria)

    # Process each line in the PDB file
    for line in data:
        print(line)
        if line.startswith('ATOM'):
            atom_index = int(line[6:11].strip())
            atom_name = line[12:16].strip()
            residue_number = int(line[22:26].strip())
            
            # Generate the atom description for matching
            atom_desc = f"resid {residue_number} and name {atom_name}"
            
            # Check against phi_criteria
            if atom_desc in phi_criteria:
                index = phi_criteria.index(atom_desc)
                phi_indices[index] = f'{atom_index}'               
            # Check against psi_criteria
            if atom_desc in psi_criteria:
                index = psi_criteria.index(atom_desc)
                psi_indices[index] = f'{atom_index}'
               
    
    return [phi_indices, psi_indices]

# Usage
pdb_filename = "bDGlc14bDGal.pdb"
linkages = get_linkages(pdb_filename)
print("Phi indices:", linkages[0])
print("Psi indices:", linkages[1])
