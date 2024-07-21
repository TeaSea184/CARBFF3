#!/bin/bash
REMOTE_USER=$1
MOLECULE=$2
MOLECULE_PATH=$3
cd /home/${REMOTE_USER}/Simulations/ 
unzip "${MOLECULE}.zip"
##cd /home/${MOLECULE_PATH}/${MOLECULE}/${MOLECULE}/
sbatch runPMF.sh