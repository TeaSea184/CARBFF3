# Load your PDB file in VMD
mol new bDGlc14bDGal.pdb type pdb

# Define the donor and acceptor residues and the specific atoms involved in the linkage
set donor_residue 2
set acceptor_residue 1
set donor_atom_names {H1 C1}
set acceptor_atom_names {C1 O4}

# Function to select atoms and retrieve indices
proc select_and_get_indices {resid atom_names} {
    set indices {}
    foreach atom_name $atom_names {
        set sel [atomselect top "resid $resid and name $atom_name"]
        lappend indices [lindex [$sel get index] 0]
        $sel delete
    }
    return $indices
}

# Get indices for phi and psi
set phi_indices [select_and_get_indices $donor_residue $donor_atom_names]
set psi_indices [select_and_get_indices $acceptor_residue $acceptor_atom_names]

# Output the indices of the atoms involved in the glycosidic linkage
puts "indices_phi: $phi_indices"
puts "indices_psi: $psi_indices"

# Exit VMD
exit
