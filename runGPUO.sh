#!/bin/sh
#SBATCH --account=gpuo --partition=gpuo
###for hpc node s  --account=compsci --partition=ada etc etc
#SBATCH --nodelist=srvcntgpu004
#SBATCH --nodes=1 --ntasks=20 --gres=gpu:kepler:2
#SBATCH --time=48:00:00
#SBATCH --mem-per-cpu=2000
#SBATCH --job-name="bDGlc14bDGal_PMF"
##SBATCH --dependency=afterok:
#SBATCH --mail-user=CLSTAY002@myuct.ac.za
#SBATCH --mail-type=ALL


cd /scratch/clstay002@myuct.ac.za/Simulations
#When running CUDA NAMD always add +idlepoll to the command line. This is needed to poll the GPU for results rather than sleeping while idle.
export LD_LIBRARY_PATH=/opt/exp_soft/NAMD_2.14_Linux-x86_64-multicore-CUDA/:$LD_LIBRARY_PATH
/opt/exp_soft/NAMD_2.14_Linux-x86_64-multicore-CUDA/namd2 +p20 +idlepoll +noAnytimeMigration +setcpuaffinity +isomalloc_sync run.conf > bDGlc14bDGal.log





