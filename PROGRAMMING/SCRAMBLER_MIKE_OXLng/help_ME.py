import base64
import random
import string

def my_encode(s):
    return base64.b64encode(s.encode()).decode()

def my_decode(s):
    return base64.b64decode(s.encode()).decode()

def my_scramble(s):
    return ''.join(random.sample(s, len(s)))

def my_unscramble(s):# ¯\_(ツ)_/¯  implement this function
    # Build This Func

    pass

def generate_my_secret(): 
    my_alphabet = string.ascii_letters + string.digits
    my_key = my_scramble(my_alphabet)
    my_message = "My secret code is: " + my_key
    my_encrypted = my_encode(my_message)
    return my_encrypted

my_secret = generate_my_secret()
print(my_secret)

#original_key = my_unscramble(my_secret)
print("Original Key:", original_key)
