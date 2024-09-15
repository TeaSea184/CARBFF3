#!/bin/bash

REMOTE_HOST="hpc.uct.ac.za"
MOLECULE="$1"
MOLECULE_PATH="$2"
REMOTE_USER="$3"
PASSWORD="$4"
EMAIL="$5"
#echo "Molecule: $MOLECULE"
#echo "Molecule Path: $MOLECULE_PATH"

if [ ! -d "$MOLECULE_PATH/$MOLECULE" ]; then
    mkdir -p "$MOLECULE_PATH/$MOLECULE"
fi

if [[ -z "$MOLECULE" ]]; then
    echo "Molecule variable is empty"
else
    #echo "Name variable is not empty"

    #make a copy of the simulation files for each molecule
    cp Simulation_Files/*  "$MOLECULE_PATH/${MOLECULE}/"

    # Run CarbBuilder
    python3 -qq runCarbBuilder.py "${MOLECULE}" > "$MOLECULE_PATH/${MOLECULE}/${MOLECULE}.log"

    if [ -f ${MOLECULE}_prePSFgen.pdb ]; then
        rm "${MOLECULE}_prePSFgen.pdb"
    fi  # <-- Added missing 'fi' here

    if [ -f "$MOLECULE.pdb" ]; then
        mv "$MOLECULE.pdb" "$MOLECULE_PATH/$MOLECULE/"
        mv "$MOLECULE.psf" "$MOLECULE_PATH/$MOLECULE/"

        output=""
        output=$(python3 -qq indices.py "$MOLECULE_PATH/${MOLECULE}/${MOLECULE}.pdb")

        REMOTE_PATH="${REMOTE_USER}@${REMOTE_HOST}:/home/${REMOTE_USER}/Simulations/${MOLECULE}/"

        python3 -qq updateRunFiles.py "$MOLECULE" "$output" "$EMAIL" "$REMOTE_PATH" "$MOLECULE_PATH"

        # Zip the contents
        zip -r -qq "$MOLECULE_PATH/${MOLECULE}/${MOLECULE}.zip" "$MOLECULE_PATH/${MOLECULE}/"

        sshpass -p ${PASSWORD} scp -r -q "${MOLECULE_PATH}/${MOLECULE}/${MOLECULE}.zip" "${REMOTE_USER}@${REMOTE_HOST}:/home/${REMOTE_USER}/Simulations/${MOLECULE}.zip" 
        # Log onto the remote server
        
        sshpass -p  ${PASSWORD} ssh -t -q -o StrictHostKeyChecking=no "${REMOTE_USER}@${REMOTE_HOST}" \
           "cd /home/${REMOTE_USER}/Simulations/ && \
            unzip -qq ${MOLECULE}.zip && \
           cd ${MOLECULE_PATH}/${MOLECULE}"

        sshpass -p  "${PASSWORD}" ssh -t -q "${REMOTE_USER}@${REMOTE_HOST}"<<EOF

        cd "Simulations/${MOLECULE_PATH}/${MOLECULE}" &&
        chmod +r par_all36_carb_altered_ribitol.txt &&
        chmod +rwx runPMF.sh &&
        sbatch runPMF.sh
EOF
    echo Submitted PMF calcualtion for ${MOLECULE}
    fi
fi
