def rotate_char(char, shift):
    if '!' <= char <= '~':
        return chr(((ord(char) - ord('!') + shift) % 94) + ord('!'))
    else:
        return char

def encrypt_string(input_string):
    encrypted_string = ""
    for i in range(len(input_string)):
        if i % 2 == 0:
            encrypted_char = rotate_char(input_string[i], 1)
        else:
            encrypted_char = rotate_char(input_string[i], 47)
        encrypted_string += encrypted_char
    return encrypted_string

def decrypt_string(encrypted_string):
    decrypted_string = ""
    for i in range(len(encrypted_string)):
        if i % 2 == 0:
            decrypted_char = rotate_char(encrypted_string[i], -1)
        else:
            decrypted_char = rotate_char(encrypted_string[i], -47)
        decrypted_string += decrypted_char
    return decrypted_string


input_string = "EspionageCTF{r0t_m@Y_N0t_b3_rEc1pROC@teD_5omEt1M3s}"
encrypted_result = encrypt_string(input_string)
print(encrypted_result)
decrypted_result = decrypt_string(encrypted_result)
print(decrypted_result)
