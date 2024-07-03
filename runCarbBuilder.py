import os
import subprocess
import threading
import shutil
import sys
import re
#non-repeating linkage example: bDGlc(1->4)bDGal


molecule = "bDGlc(1->4)bDGal"
#molecule = sys.argv[1]
print(molecule)
molecule_name = molecule.replace("(",'')
molecule_name = molecule_name.replace(")",'')
molecule_name = molecule_name.replace("-",'')
molecule_name = molecule_name.replace(".",'')
molecule_name = molecule_name.replace(">",'')
print(molecule_name)
adjacent_digits = re.findall(r'\d', molecule_name)
digits = [int(num) for num in adjacent_digits]
fst  = digits[0]
snd = digits[1]
convert = re.sub(r'(\w+)(\d)(\d)(\w+)', rf'\1({fst}->{snd})\4', molecule_name)

#remove linkage numbers
linkage = [int(i) for i in molecule.split() if i.isdigit()]


if os.name == 'nt':
    command = f"CBv2.1.45\\CBv2.1.45\\CarbBuilder2.exe -i \"{convert}\" -o {molecule_name} -PSF"
else:
   command = f'mono CBv2.1.45/CBv2.1.45/CarbBuilder2.exe -i "{convert}" -o {molecule_name}'

print(command)

#run CarbBuiler to generate PMFs and PSFs
try:
   result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
   print("Output:", result.stdout)
   print("Error:", result.stderr)
    
except subprocess.CalledProcessError as e:
  print(f"Command '{command}' failed with return code {e.returncode}")
  print(f"Error output: {e.stderr}")    
  result = subprocess.run(command, shell =True, check =True, )







