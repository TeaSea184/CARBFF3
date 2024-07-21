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

        bash script.sh "$mod_input" "$MOLECULE_PATH" "$REMOTE_USER" "$PASSWORD" "$EMAIL"  
    linkage_output=$(python3 DisaccharideSeparator.py "$MOLECULE")
    IFS=, read -ra linkages <<< "$(echo "$linkage_output" | sed 's/\[\][\]//g')"

    for element in "${linkages[@]}"; do  
        link=$(echo "$element" | sed "s/'//g" | awk -F'[][]' '{print $2}')
        updated_link=$(echo "$link" | sed 's/[-()>]//g')
        bash script.sh "$updated_link" "$MOLECULE_PATH" "$REMOTE_USER" "$PASSWORD" "$EMAIL"  
    done
fi

