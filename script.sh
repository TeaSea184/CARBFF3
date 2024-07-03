#!/bin/bash

echo Enter the molecule
read MOLECULE
hostname=$(hostname)
echo Enter your account username
read REMOTE_USER
REMOTE_HOST="hpc.uct.ac.za"
echo Enter your password
read PASSWORD

echo Enter email
read EMAIL

if [ ! -d output/$MOLECULE ]; then
    mkdir -p output/$MOLECULE
fi

## Run CarbBuilder
python3 runCarbBuilder.py $MOLECULE > output/${MOLECULE}/${MOLECULE}.log

mv $MOLECULE.pdb output/$MOLECULE/
mv $MOLECULE.psf output/$MOLECULE/

output=$(python3 indices.py output/${MOLECULE}/${MOLECULE}.pdb)
echo "output: $output"
REMOTE_PATH = "${REMOTE_USER}@${REMOTE_HOST}://home/${REMOTE_USER}/Simulations/${MOLECULE}/"
python3 updateRunFiles.py "$MOLECULE" "$output" "$EMAIL" "$REMOTE_PATH"

## Zip the contents
zip -r output/${MOLECULE}/${MOLECULE}.zip output/${MOLECULE}/*

# Log onto the remote server
sshpass -p "$PASSWORD" ssh "${REMOTE_USER}@${REMOTE_HOST}"

#move zip file
scp -r output/${MOLECULE}.zip ${REMOTE_USER}@${REMOTE_HOST}://home/${REMOTE_USER}/Simulations/${MOLECULE}/