#!/bin/bash

echo "Enter the molecule"
read MOLECULE
start=1
iterations=5
MOLECULE_PATH=$(echo "output/$MOLECULE" | sed 's/[-()>]//g')  # Set once at the top

if [[ "$MOLECULE" == *'*'* ]]; then
    for ((i=1; i<=$iterations; i++)); do
        number=$((start + i))  # Ensure 'start' is defined
        mod_input=$(echo "$MOLECULE" | sed "s/\*/$number/g")  # Use double quotes for variable expansion

        bash script.sh "$mod_input" "$MOLECULE_PATH"  # Ensure space between arguments
    done
else
    linkage_output=$(python3 DisaccharideSeparator.py "$MOLECULE")
    IFS=, read -ra linkages <<< "$(echo "$linkage_output" | sed 's/\[\][\]//g')"

    for element in "${linkages[@]}"; do  # Use '@' to expand the array correctly
        link=$(echo "$element" | sed "s/'//g" | awk -F'[][]' '{print $2}')
        updated_link=$(echo "$link" | sed 's/[-()>]//g')
        bash script.sh "$updated_link" "$MOLECULE_PATH"  # Ensure variable is quoted
    done
fi

