import MDAnalysis as mda
import re
import sys
def get_glycosidic_indices(pdb_file):
    print("Executing get_glycosidic_indices")
    # Load the PSF and PDB files
    u = mda.Universe(pdb_file)

        # Find atoms with unknown elements
    unknown_elements = [atom for atom in u.atoms if atom.element == '']
    if unknown_elements:
        print("Unknown elements found:")
        for atom in unknown_elements:
            print(f"Atom {atom.name} in residue {atom.resname}{atom.resid} has an unknown element.")
    else:
        print("No unknown elements found.")

    residues = u.residues
    res_names = [residue.resname for residue in residues]
    print(res_names)
    
    # Get linkage numbers from the filename
    linkage = re.findall(r'\d', u.filename)
    print(linkage)
    

    fst = linkage[0]
    snd = linkage[1]
    # phi - H1 C1 O4 C4
    #psi - C1 O4 C4 H4
    # Define the atom selection criteria in the desired order
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

    def select_and_get_indices(criteria):
        indices = []
        #return NAMD indices
        if phi_criteria and psi_criteria != '{}':
            for criterion in criteria:
                atom = u.select_atoms(criterion)
                indices.append(atom.indices[0]+1)  # Convert to 1-based indexing
            return indices

    # Get indices for phi and psi
    indices_phi = select_and_get_indices(phi_criteria)
    indices_psi = select_and_get_indices(psi_criteria)
    
    print(f"indices_phi: {indices_phi}")
    print(f"indices_psi: {indices_psi}")

    return [indices_phi, indices_psi]

if __name__ == "__main__":
    filename = sys.argv[1]
    indices= get_glycosidic_indices(filename)
    phi_indices = indices[0]
    psi_indices = indices[1]

# Example usage
#pdb_file = 'pdb_files\\bDGlc14bDGal.pdb'
#psf_file = 'test.psf'
#print(get_glycosidic_indices(pdb_file))
#print(get_glycosidic_indices(pdb_file)[0])
