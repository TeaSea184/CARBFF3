import re

# Original string
input_string = "->2)aLRha(1->2)aLRha(1->3)aLRha(1->3)bDGlcNAc(1->"
print(input_string[-1])
# Define a general pattern to capture substrings with specific structure
# This example assumes a general pattern, adjust as needed
pattern = r'\w+\(\d+->\d+\)\w+'

# Extract substrings based on the pattern
extracted_substrings = re.findall(pattern, input_string)

# Print the extracted substrings
for substring in extracted_substrings:
    print(substring)
