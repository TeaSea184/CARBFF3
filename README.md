This system allows for the calculation of PMF values for polysaccahride structures in the CASPER format.

This system is implemented using bash shell scripts Python 3.10.12 scripts and uses the CarbBuilder v1.2.45 software to build molecule files. 

A University of Cape Town(UCT) High Performance Computing(HPC) account is required and users should run this system on UCT's network.

For more information about UCT's HPC cluster visit: 
https://ucthpc.uct.ac.za/ 

SYSTEM
Files contained in this system:
input.sh
DissacharideSeparator.py
script.sh
runCarbBuilder.py
indices.py
updateRunFiles.py


EXECUTION
Run the file input.sh through a Linux terminal with the command
bash input.sh and enter the name of the molecule in CASPER format.

The system takes two types of input in the CASPER format:
1. Polysachharide structures: e.g. ->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlcNAc(1->
2. 'Wildcard' linkages e.g. bDGlc(1->*)bDGal

Enter your UCT HPC account username and password, and an email address.

For example:
Enter the molecule
>>bDGlc(1->*)bDGal
Enter your username
>>username
Enter your password
>>password
Enter your email address
>>myemail@myuct.ac.za

The system will run CarBuilder to build the models of the disaccharides that are obtained by separating the polysaccharide or substituting the '*' with the numbers 2-6, then update the simulation files and run the PMF calculations on UCT's HPC cluster.

NOTE: On Linux machines CarbBuilder requires the installation of the mono framework

For more information about CarbBuider and the CASPER format visit:
https://people.cs.uct.ac.za/~mkuttel/installCB2.html





