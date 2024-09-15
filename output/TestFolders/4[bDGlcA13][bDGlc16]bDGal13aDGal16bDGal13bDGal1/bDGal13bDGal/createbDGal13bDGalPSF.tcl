package require psfgen

resetpsf
topology /home/vboxuser/Documents/HonsProject/Code/CHARMM_topology_file.txt


segment CARB {pdb bDGlc14bDGal.pdb}

patch 13bb CARB:1 CARB:2


coordpdb bDGlc14bDGal.pdb CARB

regenerate angles dihedrals


writepsf ouput.psf


# Exit psfgen
exit