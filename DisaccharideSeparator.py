import regex as re

#input format: bDGlc(1->4)bDGal
#For individual polsaccharide molecules:"->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlcNAc(1->"
#linkages: aLRha(1->2)aLRha , aLRha(1->3)aLRha, aLRha(1->3)bDGlcNAc, bDGlcNAc(1->2)aLRha)
molecule= "->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlcNAc(1->"
last_linkage = molecule[2:9]

if molecule[0] == '-':
    molecule = last_linkage[2:]+molecule[9:] + last_linkage
    
#molecule = molecule.replace("(","")
#molecule = molecule.replace(")","")
#molecule = molecule.replace("-","")
#molecule = molecule.replace(">","")
print(molecule)
#molecule = 2aLRha12aLRha13aLRha13bDGlcNAc1
#molecule = 2aLRha12aLRha13aLRha13bDGlcNAc1
#disaccharides = aLRha12aLRha, aLRha13aLRha, aLRha13bDGlcNAc, bDGlcNAc12aLRha

mol_pattern = r'\([^)]+\)'
# Replace the content within the brackets with a space
mono = re.sub(mol_pattern, ' ', molecule)

monosaccharides = mono.split()
print(monosaccharides)
# Define a regular expression pattern to match the disaccharide linkages
pattern = r'[a-zA-Z]+\(\d+->\d+\)[a-zA-Z]+'

# Find all matches of the pattern in the polysaccharide string
disaccharide_linkages = re.findall(pattern, molecule, overlapped=True)
final = []
for d in disaccharide_linkages:
    if d[:d.index('(')] in monosaccharides:
        final.append(d)
print(final)#input format: bDGlc(1->4)bDGal
#For individual polsaccharide molecules:"->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlcNAc(1->"
#linkages: aLRha(1->2)aLRha , aLRha(1->3)aLRha, aLRha(1->3)bDGlcNAc, bDGlcNAc(1->2)aLRha)
molecule= "->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlcNAc(1->"
last_linkage = molecule[2:9]

if molecule[0] == '-':
    molecule = last_linkage[2:]+molecule[9:] + last_linkage
    
#molecule = molecule.replace("(","")
#molecule = molecule.replace(")","")
#molecule = molecule.replace("-","")
#molecule = molecule.replace(">","")
print(molecule)
#molecule = 2aLRha12aLRha13aLRha13bDGlcNAc1
#molecule = 2aLRha12aLRha13aLRha13bDGlcNAc1
#disaccharides = aLRha12aLRha, aLRha13aLRha, aLRha13bDGlcNAc, bDGlcNAc12aLRha

mol_pattern = r'\([^)]+\)'
# Replace the content within the brackets with a space
mono = re.sub(mol_pattern, ' ', molecule)

monosaccharides = mono.split()
print(monosaccharides)
# Define a regular expression pattern to match the disaccharide linkages
pattern = r'[a-zA-Z]+\(\d+->\d+\)[a-zA-Z]+'

# Find all matches of the pattern in the polysaccharide string
disaccharide_linkages = re.findall(pattern, molecule, overlapped=True)
final = []
for d in disaccharide_linkages:
    if d[:d.index('(')] in monosaccharides:
        final.append(d)
print(final)#input format: bDGlc(1->4)bDGal
#For individual polsaccharide molecules:"->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlcNAc(1->"
#linkages: aLRha(1->2)aLRha , aLRha(1->3)aLRha, aLRha(1->3)bDGlcNAc, bDGlcNAc(1->2)aLRha)
molecule= "->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlcNAc(1->"
last_linkage = molecule[2:9]

if molecule[0] == '-':
    molecule = last_linkage[2:]+molecule[9:] + last_linkage
    
#molecule = molecule.replace("(","")
#molecule = molecule.replace(")","")
#molecule = molecule.replace("-","")
#molecule = molecule.replace(">","")
print(molecule)
#molecule = 2aLRha12aLRha13aLRha13bDGlcNAc1
#molecule = 2aLRha12aLRha13aLRha13bDGlcNAc1
#disaccharides = aLRha12aLRha, aLRha13aLRha, aLRha13bDGlcNAc, bDGlcNAc12aLRha

mol_pattern = r'\([^)]+\)'
# Replace the content within the brackets with a space
mono = re.sub(mol_pattern, ' ', molecule)

monosaccharides = mono.split()
print(monosaccharides)
# Define a regular expression pattern to match the disaccharide linkages
pattern = r'[a-zA-Z]+\(\d+->\d+\)[a-zA-Z]+'

# Find all matches of the pattern in the polysaccharide string
disaccharide_linkages = re.findall(pattern, molecule, overlapped=True)
final = []
for d in disaccharide_linkages:
    if d[:d.index('(')] in monosaccharides:
        final.append(d)
print(final)#input format: bDGlc(1->4)bDGal
#For individual polsaccharide molecules:"->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlcNAc(1->"
#linkages: aLRha(1->2)aLRha , aLRha(1->3)aLRha, aLRha(1->3)bDGlcNAc, bDGlcNAc(1->2)aLRha)
molecule= "->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlcNAc(1->"
last_linkage = molecule[2:9]

if molecule[0] == '-':
    molecule = last_linkage[2:]+molecule[9:] + last_linkage
    
#molecule = molecule.replace("(","")
#molecule = molecule.replace(")","")
#molecule = molecule.replace("-","")
#molecule = molecule.replace(">","")
print(molecule)
#molecule = 2aLRha12aLRha13aLRha13bDGlcNAc1
#molecule = 2aLRha12aLRha13aLRha13bDGlcNAc1
#disaccharides = aLRha12aLRha, aLRha13aLRha, aLRha13bDGlcNAc, bDGlcNAc12aLRha

mol_pattern = r'\([^)]+\)'
# Replace the content within the brackets with a space
mono = re.sub(mol_pattern, ' ', molecule)

monosaccharides = mono.split()
print(monosaccharides)
# Define a regular expression pattern to match the disaccharide linkages
pattern = r'[a-zA-Z]+\(\d+->\d+\)[a-zA-Z]+'

# Find all matches of the pattern in the polysaccharide string
disaccharide_linkages = re.findall(pattern, molecule, overlapped=True)
final = []
for d in disaccharide_linkages:
    if d[:d.index('(')] in monosaccharides:
        final.append(d)
print(final)