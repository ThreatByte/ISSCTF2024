#!/bin/bash

#the number list goes in numbers()
id=()

string=""

for num in "${horde[@]}"; do
  string="${string}$(printf "\\$(printf '%03o' "$num")")"
done

# Print the resulting string
echo "$string"

#to find the flag they can either look at the output or pipe the output to a text and use grep to get the flag
