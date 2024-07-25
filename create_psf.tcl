# Load topology and parameter files
topology CHARMM_topology_file.txt

# Define segment for the disaccharide
segment disaccharide {
    pdb Code/bDGlc14bDGal.pdb
}

segment CARB { first NONE; last NONE; auto angles dihedrals }
patch 14BA CARB:1  CARB:2  

package require psfgen

# Set phi angle
setattr dihedral {disaccharide H1 C1 O4 C4} 

# Set psi angle
setattr dihedral {disaccharide C1 O4 C4 H4} 


set psf_output_file "/home/vboxuser/Documents/HonsProject/Code/output.psf"
writepsf $psf_output_file

# Exit psfgen
exit
