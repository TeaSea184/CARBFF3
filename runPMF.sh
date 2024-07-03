#!/bin/sh
#SBATCH --account=gpumk --partition=gpumk
###for hpc node s  --account=compsci --partition=ada etc etc
#SBATCH --nodes=1 --ntasks=20 --gres=gpu:2 
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=2000
#SBATCH --job-name="bRha14bGlc_PMF"
#SBATCH --mail-user=YRLNIC001@myuct.ac.za
#SBATCH --mail-type=ALL


cd /scratch/yrlnic001/Pn23_bRha14bGlc
#When running CUDA NAMD always add +idlepoll to the command line. This is needed to poll the GPU for results rather than sleeping while idle.
#export LD_LIBRARY_PATH=/opt/exp_soft/NAMD_2.13_Linux-x86_64-multicore-CUDA/:$LD_LIBRARY_PATH
/opt/exp_soft/NAMD_2.13_Linux-x86_64-multicore-CUDA/namd2 run.conf > run1.log


