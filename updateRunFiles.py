import re
import fileinput
import shutil
#from  GlycoIndices import get_glycosidic_indices
import os
import sys
import ast

def updateRunFiles(molecule_name, phi, psi, email, path, mol_path):
    print(phi)
    print(psi)
    print("Executing updateRunFiles")
#read in all files  
    output = f"{mol_path}/{molecule_name}"
    print(output)
    os.makedirs(output, exist_ok=True)
    #create a copy and update run.conf
    shutil.copy("run.conf", f"{output}/run.conf")    
    for line in fileinput.input(f"{output}/run.conf", inplace=True):
        if line.startswith('coordinates'):
            print (f"coordinates      {molecule_name}.pdb")
        elif line.startswith('structure'):
            print(f"structure        {molecule_name}.psf")
        elif line.startswith('set output'):
            print(f"set output       {molecule_name}_PMF")
        elif line.startswith('restartname'):
            print(f"restartname      {molecule_name}_PMF")
        else: 
            print(line,end='')

    index = 0 
    angle = None
    #create a copy and update colvars.txt
    shutil.copy("colvars.txt", f"{output}/colvars.txt")
    for line in fileinput.input(f"{output}/colvars.txt", inplace=True):
        if line.strip().startswith("name"):
            angle = line.strip().split()[1]
            index =0
            print(line,end='')
        elif line.strip().startswith("atomnumbers"):
            if angle == 'Phi' and index < len(phi):
                print(f"            atomnumbers { {phi[index]} }")
            elif angle == 'Psi'and index < len(psi):
                print(f"            atomnumbers { {psi[index]} }")
            else:
                print(line,end='')
            index+=1
        else:
            print(line,end='')

    #copy over parameter file 
    shutil.copy(f"par_all36_carb_altered_ribitol.txt",f"{output}/par_all36_carb_altered_ribitol")
    
    shutil.copy("runPMF.sh", f"{output}/runPMF.sh")

    for line in fileinput.input(f"{output}/runPMF.sh", inplace=True):
        if line.startswith("#SBATCH --mail-user"):
            print(f"#SBATCH --mail-user= {email}")
        elif line.startswith("#SBATCH --job-name="):
            print(f"#SBATCH --job-name= \"{molecule_name}_PMF\"")
        elif line.strip().startswith("cd"):
            print(f"cd {path}/{molecule_name}")
        elif line.strip().startswith("/opt/exp_soft/NAMD_2.13_Linux-x86_64-multicore-CUDA/namd2run.conf>"):
            print(f"/opt/exp_soft/NAMD_2.13_Linux-x86_64-multicore-CUDA/namd2 run.conf > run{molecule_name}.log")
        else:
            print(line, end='')

if __name__ == "__main__":
    print(sys.argv)
    name = sys.argv[1]
    output = ast.literal_eval(sys.argv[2])
    email = sys.argv[3]
    print(f"Email: {email}")
    path = sys.argv[4]
    print(f"Path: {path}")
    phi = output[0]
    psi = output[1]
    mol_path =sys.argv[5]
    updateRunFiles(name,phi,psi,email,path, mol_path)
#Example usage
#atom_numbers = get_glycosidic_indices("pdb_files\\bDGlc14bDGal.pdb")
#phi = atom_numbers[0]
#psi = atom_numbers[1]
#name = "bDGlc14bDGal"
#updateRunFiles(name,phi,psi)