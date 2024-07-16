#!/bin/bash

MOLECULE="$1"
MOLECULE_PATH="$2"

echo "Molecule: $MOLECULE"
echo "Molecule Path: $MOLECULE_PATH"

echo "Enter your account username:"
read REMOTE_USER
REMOTE_HOST="hpc.uct.ac.za"
echo "Enter your password:"
read -s PASSWORD  # Use -s to hide the password input

echo "Enter email:"
read EMAIL

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

# Zip the contents
zip -r "$MOLECULE_PATH/${MOLECULE}/${MOLECULE}.zip" "$MOLECULE_PATH/${MOLECULE}/"

# Log onto the remote server
ssh "${REMOTE_USER}@${REMOTE_HOST}" << EOF
    scp -r "${MOLECULE_PATH}/${MOLECULE}/${MOLECULE}.zip" "${REMOTE_USER}@${REMOTE_HOST}:/home/${REMOTE_USER}/Simulations/${MOLECULE}.zip"
    cd /home/${REMOTE_USER}/Simulations/ 
    unzip "${MOLECULE}.zip"
EOF
