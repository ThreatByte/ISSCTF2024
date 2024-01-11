import random

def SCRAMBLER(s):
    J_pairs = ""
    shuffled_chars = list(s)
    for i in range(len(shuffled_chars) - 1, 0, -1):
        J = random.randint(0, i)
        # Store the pair of indices (i, J)
        J_pairs += f"{i},{J};"
        shuffled_chars[i], shuffled_chars[J] = shuffled_chars[J], shuffled_chars[i]
    # Append the J_pairs string to the scrambled string separated by a unique delimiter
    return ''.join(shuffled_chars) + "#DELIM#" + J_pairs

def UNSCRAMBLER(combined_s):
    # Split the input string to get the scrambled part and the J_pairs
    scrambled, j_pairs_str = combined_s.split("#DELIM#")
    unscrambled_chars = list(scrambled)
    # Convert the J_pairs string back into a list of tuples
    J_pairs_list = [tuple(map(int, pair.split(','))) for pair in j_pairs_str.strip(";").split(";")][::-1]
    for i, J in J_pairs_list:
        unscrambled_chars[i], unscrambled_chars[J] = unscrambled_chars[J], unscrambled_chars[i]
    return ''.join(unscrambled_chars)

# Example Usage

unscrambled_flag = UNSCRAMBLER("EIiaGBSCF{_EMLEATGngeSeLpo_DCki_s}R#DELIM#34,22;33,22;32,1;31,19;30,16;29,17;28,21;27,21;26,14;25,4;24,2;23,15;22,18;21,20;20,8;19,7;18,5;17,1;16,10;15,15;14,10;13,10;12,2;11,8;10,1;9,2;8,8;7,2;6,5;5,4;4,2;3,2;2,2;1,1;")

# Print statements

print("Unscrambled Flag:", unscrambled_flag)
