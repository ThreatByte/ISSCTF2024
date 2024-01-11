def encrypt(message, key):
    adjusted_key = key + [key[0]] if len(message) > len(key) else key
    return [(m + k) % 26 for m, k in zip(message, adjusted_key)]

def decrypt(encrypted_message, key):
    adjusted_key = key + [key[0]] if len(encrypted_message) > len(key) else key
    return [(m - k) % 26 for m, k in zip(encrypted_message, adjusted_key)]

# Converting letters to numbers
message = [25, 5, 12, 12, 15, 23, 11, 14, 9, 6, 5]  # Y E L L O W K N I F E
key = [13, 20, 23, 5, 14, 20, 25, 19, 9, 24]        # M T W E N T Y S I X

# Encrypt the message
encrypted_message = encrypt(message, key)
print("Encrypted Message (in numbers):", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted Message (in numbers):", decrypted_message)



