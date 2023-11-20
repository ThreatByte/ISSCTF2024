import random
import string


def SCRAMBLER(s):
    return ''.join(random.sample(s, len(s)))

def UNSCRAMBLER(s):# ¯\_(ツ)_/¯  implement this function
    # Build This Func

    pass

def generate_my_secret(): 
    alphabet = string.ascii_letters + string.digits
    key = SCRAMBLER(alphabet)
    message = "My secret code is: " + key
    encrypted = SCRAMBLER(message)
    return encrypted

hidden = generate_my_secret()

#original_key = UNSCRAMBLER(hidden) #uncomment after 
print("Original Key:", hidden)
