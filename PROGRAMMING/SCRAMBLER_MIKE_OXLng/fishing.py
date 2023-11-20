import string

def SCRAMBLER(s):
    # Using  the fis... shuffle algorithm for shuffling
    shuffled_chars = list(s)
    for i in range(len(shuffled_chars) - 1, 0, -1):
        j = random.randint(0, i) # wait whut 
        shuffled_chars[i], shuffled_chars[j] = shuffled_chars[j], shuffled_chars[i]
    return ''.join(shuffled_chars)


def UNSCRAMBLER(s): # ¯\_(ツ)_/¯ implement this function
    #BUIL:D me ...!!!!!!!!!!!!!!!!!!!!!

    return 

def generate_my_secret(): 
    # The flag to be scrambled
    flag = "EspionageCTF{I_Like_SCRAMBLED_EGGS}"
    # Scramble the flag to create a key
    key = SCRAMBLER(flag)
    # Create a message using the scrambled key
    message = "My secret code is: " + key
    # Scramble the message
    encrypted_message = SCRAMBLER(message)
    # Return the scrambled message and the key
    return encrypted_message, key

# Uncomment the line below to see the original key after unscrambling
#print("Original Key:", UNSCRAMBLER(original_key))
print("Hidden Message:", hidden)
