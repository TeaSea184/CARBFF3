import re
import sys

def get_glycosidic_indices(pdb_file):
    print("Executing get_glycosidic_indices")

    # Open the PDB file and read lines
    with open(pdb_file, 'r') as f:
        lines = f.readlines()

    # Initialize lists to store indices
    indices_phi = []
    indices_psi = []

    # Define regular expressions to match atom lines
    atom_pattern = re.compile(r'^ATOM\s+\d+\s+(\S+)\s+(\S+)(\d+)\s+(\S+)\s+(\S+\s+\S+\s+\S+)\s+')

    # Iterate through lines to find relevant atoms
    for line in lines:
        match = atom_pattern.match(line)
        if match:
            atom_name = match.group(2)
            residue_name = match.group(4)
            residue_number = int(match.group(3))

            # Determine if the atom is part of the criteria for phi or psi
            if atom_name.startswith('H') and residue_number == 2:
                if atom_name[1:].isdigit():
                    fst = int(atom_name[1:])
                    indices_phi.append(fst)
            elif atom_name.startswith('C') and residue_number == 2:
                if atom_name[1:].isdigit():
                    fst = int(atom_name[1:])
                    indices_phi.append(fst)
            elif atom_name.startswith('O') and residue_number == 1:
                if atom_name[1:].isdigit():
                    snd = int(atom_name[1:])
                    indices_phi.append(snd)
            elif atom_name.startswith('C') and residue_number == 1:
                if atom_name[1:].isdigit():
                    snd = int(atom_name[1:])
                    indices_phi.append(snd)

    print(f"indices_phi: {indices_phi}")
    print(f"indices_psi: {indices_psi}")

    return [indices_phi, indices_psi]

if __name__ == "__main__":
    filename = sys.argv[1]
    indices = get_glycosidic_indices(filename)
    phi_indices = indices[0]
    psi_indices = indices[1]

    # Example usage
    # pdb_file = 'pdb_files\\bDGlc14bDGal.pdb'
    # print(get_glycosidic_indices(pdb_file))
    # print(get_glycosidic_indices(pdb_file)[0])
