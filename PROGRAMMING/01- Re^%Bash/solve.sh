#!/bin/bash


numbers=("69" "115" "112" "105" "111" "110" "97" "103" "101" "67" "84" "70" "123" "66" "97" "115" "104" "95" "83" "99" "114" "105" "112" "116" "105" "110" "103" "95" "73" "115" "95" "83" "117" "112" "101" "114" "95" "104" "97" "110" "100" "121" "121" "125")

string=""

for num in "${numbers[@]}"; do
  string="${string}$(printf "\\$(printf '%03o' "$num")")"
done

# Print the resulting string
echo "$string"






