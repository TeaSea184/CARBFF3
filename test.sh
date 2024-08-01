MOLECULE='->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlc(1->'

linkage_output=$(python3 DisaccharideSeparator.py "${MOLECULE}")
IFS=, read -ra linkages <<< "$(echo "$linkage_output" | sed 's/\[\][\]//g')"

for element in "${linkages[@]}"; do  
    echo Element:$element
    link=$(echo "$element" | sed "s/'//g" | awk -F'[][]' '{print $2}')
    updated_link=$(echo "$link" | sed 's/[-()>]//g')
    echo $updated_link
done