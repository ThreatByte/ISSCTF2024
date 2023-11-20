import random
import string

# Global variable for j
J = random.randint(0, 1)

def SCRAMBLER(s):
    # Randomly shuffle the characters in the input string 's'
    # Use the Fisher-Yates shuffle algorithm for deterministic shuffling
    shuffled_chars = list(s)
    for i in range(len(shuffled_chars) - 1, 0, -1):
        shuffled_chars[i], shuffled_chars[J] = shuffled_chars[J], shuffled_chars[i]
    return ''.join(shuffled_chars)
    

def UNSCRAMBLER(s): # ¯\_(ツ)_/¯ implement this function
  # Use the Fisher-Yates shuffle algorithm to deterministically unscramble the characters in the input string 's'
    unscrambled_chars = list(s)
    for i in range(len(unscrambled_chars) - 1, 0, -1):
        j = i
        while j == i:
            j = random.randint(0, i)
        unscrambled_chars[i], unscrambled_chars[J] = unscrambled_chars[J], unscrambled_chars[i]
    return ''.join(unscrambled_chars)

    
def generate_my_secret(): 
    # The flag to be scrambled
    flag = "EXAMPLE"#put hidden message we captured here when ready
    # Scramble the flag to create a key
    key = SCRAMBLER(flag)
    # Create a message using the scrambled key
    message = "fishFishy" + key
    # Scramble the message
    encrypted_message = SCRAMBLER(message)
    # Return the scrambled message and the key
    return encrypted_message, key

# Generate the secret and get the scrambled message and key
hidden, original_key = generate_my_secret()

# Uncomment the line below to see the original key after unscrambling
print("Original Key:", UNSCRAMBLER(original_key))
print("Hidden Message:", hidden)


'''
EXAMPLE OUTPUT FROM THIS CODE:

Original Key: AMPLEEX
Hidden Message: ishFishyXAMPLEEf

'''