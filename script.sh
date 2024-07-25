#!/bin/bash

REMOTE_HOST="hpc.uct.ac.za"
MOLECULE="$1"
MOLECULE_PATH="$2"
REMOTE_USER="$3"
PASSWORD="$4"
EMAIL="$5"
echo "Molecule: $MOLECULE"
echo "Molecule Path: $MOLECULE_PATH"



if [ ! -d "$MOLECULE_PATH/$MOLECULE" ]; then
    mkdir -p "$MOLECULE_PATH/$MOLECULE"
fi

# Run CarbBuilder
python3 runCarbBuilder.py "$MOLECULE" > "$MOLECULE_PATH/${MOLECULE}/${MOLECULE}.log"

if [ -f "$MOLECULE.pdb" ]; then
    mv "$MOLECULE.pdb" "$MOLECULE_PATH/$MOLECULE/"
fi 

output=$(python3 indices.py "$MOLECULE_PATH/${MOLECULE}/${MOLECULE}.pdb")
echo "Output: $output"
REMOTE_PATH="${REMOTE_USER}@${REMOTE_HOST}:/home/${REMOTE_USER}/Simulations/${MOLECULE}/"

python3 updateRunFiles.py "$MOLECULE" "$output" "$EMAIL" "$REMOTE_PATH" "$MOLECULE_PATH"

#create molecule psf file
namd3 +p4 +stdout output.log "${MOLECULE_PATH}/${MOLECULE}/create${MOLECULE}PSF.tcl"
mv "/home/vboxuser/Documents/HonsProject/Code/${MOLECULE}.psf" "${MOLECULE_PATH}/${MOLECULE}/${MOLECULE}.psf"
# Zip the contents
zip -r "$MOLECULE_PATH/${MOLECULE}/${MOLECULE}.zip" "$MOLECULE_PATH/${MOLECULE}/"

sshpass -p ${PASSWORD} scp -r "${MOLECULE_PATH}/${MOLECULE}/${MOLECULE}.zip" "${REMOTE_USER}@${REMOTE_HOST}:/home/${REMOTE_USER}/Simulations/${MOLECULE}.zip" 
# Log onto the remote server
sshpass -p ${PASSWORD} ssh -o StrictHostKeyChecking=no "${REMOTE_USER}@${REMOTE_HOST}" \
    "cd /home/${REMOTE_USER}/Simulations/ && \
    unzip ${MOLECULE}.zip && \
    cd ${MOLECULE_PATH}/${MOLECULE}"

sshpass -p ${PASSWORD} ssh "${REMOTE_USER}@${REMOTE_HOST}"  cd Simulations/${MOLECULE_PATH}/${MOLECULE} && chmod +r par_all36_carb_altered_ribitol.txt && sbatch runPMF.sh

