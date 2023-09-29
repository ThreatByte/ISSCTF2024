#!/bin/bash

#the number list goes in numbers()
numbers=()

string=""

for num in "${numbers[@]}"; do
  string="${string}$(printf "\\$(printf '%03o' "$num")")"
done

# Print the resulting string
echo "$string"

#after the output, they have to search for the words which can be linked to the flag among the output
