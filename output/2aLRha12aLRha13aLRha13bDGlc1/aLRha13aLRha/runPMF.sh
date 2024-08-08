#!/bin/sh
#SBATCH --account=gpumk --partition=gpumk
###for hpc node s  --account=compsci --partition=ada etc etc
#SBATCH --nodes=1 --ntasks=2 --gres=gpu:2 
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=2000
#SBATCH --job-name= "aLRha13aLRha_PMF"
#SBATCH --mail-user= CLSTAY002@myuct.ac.za
#SBATCH --mail-type=ALL


#cd output/2aLRha12aLRha13aLRha13bDGlc1/aLRha13aLRha
#When running CUDA NAMD always add +idlepoll to the command line. This is needed to poll the GPU for results rather than sleeping while idle.
#export LD_LIBRARY_PATH=/opt/exp_soft/NAMD_2.13_Linux-x86_64-multicore-CUDA/:$LD_LIBRARY_PATH
/opt/exp_soft/NAMD_2.13_Linux-x86_64-multicore-CUDA/namd2 run.conf > runaLRha13aLRha.log


