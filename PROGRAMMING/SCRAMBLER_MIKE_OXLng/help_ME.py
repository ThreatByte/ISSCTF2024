import string

def SCRAMBLER(s)::# ¯\_(ツ)_/¯  implement this function
    # Use the Fisher-Yates shuffle algorithm for deterministic shuffling
    shuffled_chars = list(s)
    for i in range(len(shuffled_chars) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled_chars[i], shuffled_chars[j] = shuffled_chars[j], shuffled_chars[i]
    return ''.join(shuffled_chars)

# Rest of the code remains the same
# ...

# Uncomment the line below to see the original key after unscrambling
print("Original Key:", UNSCRAMBLER(original_key))
print("Hidden Message:", hidden)
