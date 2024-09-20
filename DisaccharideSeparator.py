import re
import sys

def sepDisach(mol):
    molecule= mol
    
    #For individual polsaccharide molecules:"->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlcNAc(1->"
    #linkages: aLRha(1->2)aLRha , aLRha(1->3)aLRha, aLRha(1->3)bDGlcNAc, bDGlcNAc(1->2)aLRha)

    last_linkage = molecule[2:9]
    molecule = molecule.replace('[','').replace(']','')
   
    result = ''
    if molecule[0] == '-' and molecule[-1] == '>':
        molecule = molecule[2:]
        molecule = molecule + molecule

    #remove square brackets
    
    mol_pattern = r'\([^)]+\)'
    # Replace the content within the brackets with a space
    mono = re.sub(mol_pattern, ' ', molecule)

    monos = mono.split()
   # print(monosaccharides)
    monosaccharides = []
    for x in monos:
        x = re.sub(r'^.*?\)', '', x)
        x = re.sub(r'\(.*$', '', x)
        monosaccharides.append(x)

    #Disaccharide linkages regular expression
    pattern = r'(?=(\b[a-zA-Z]+\(\d+->\d+\)[a-zA-Z]+\b))'

    # Find all matches of the pattern in the polysaccharide string
    disaccharide_linkages = re.findall(pattern, molecule)
    final = []
    seen = []
    for d in disaccharide_linkages:
        if d[:d.index('(')] in monosaccharides:
            final.append(d)

    for f in final:
        if f not in seen:
            seen.append(f)
    print(seen)

if __name__ == "__main__":
    molecule = sys.argv[1]
    sepDisach(molecule)
