#!/bin/bash

echo "Enter the molecule"
read MOLECULE
echo "Enter your account username:"
read REMOTE_USER

echo "Enter your password:"
read -s PASSWORD  # Use -s to hide the password input

echo "Enter email:"
read EMAIL
start=1
iterations=5
MOLECULE_PATH=$(echo "output/$MOLECULE" | sed 's/[-()>]//g') 
if [[ "$MOLECULE" == *'*'* ]]; then
    for ((i=1; i<=$iterations; i++)); do
        number=$((start + i))  
        mod_input=$(echo "$MOLECULE" | sed "s/\*/$number/g") 
        updated_mod=$(echo "$mod_input" | sed 's/[-()>]//g')
        #echo $mod_input
        bash script.sh "$updated_mod" "$MOLECULE_PATH" "$REMOTE_USER" "$PASSWORD" "$EMAIL"  
    done
else    
    linkage_output=$(python3 DisaccharideSeparator.py "$MOLECULE")
    IFS=, read -ra linkages <<< "$(echo "$linkage_output" | sed "s/^\[\|]$//g" | sed "s/'//g")"
    #echo $IFS
    for element in "${linkages[@]}"; do  
        link=$(echo "$element" | sed "s/'//g" | awk -F'[][]' '{print $2}')
        updated_link=$(echo "$element" | sed 's/[-()>]//g')
        #echo $updated_link
        trimmed_link=$(echo "$updated_link"|tr -d ' ')
        final_link="${trimmed_link//,/}"
        #echo $final_link
        bash script.sh "${final_link}" "$MOLECULE_PATH" "$REMOTE_USER" "$PASSWORD" "$EMAIL"  
    done
fi
#->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlc(1->

