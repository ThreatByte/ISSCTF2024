def rot47_encrypt(char, rot47_list):
    if '!' <= char <= '~':
        original_index = ord(char) - ord('!')
        return rot47_list[original_index]
    return char

def custom_rot47_encrypt(plaintext, rot47_list, reverse_rot47_list):
    ciphertext = ''

    for index, char in enumerate(plaintext):
        if index % 2 == 1:
            # Odd index, use ROT-47 with the original list
            ciphertext += rot47_encrypt(char, rot47_list)
        else:
            # Even index, use ROT-47 with the reversed list
            ciphertext += rot47_encrypt(char, reverse_rot47_list)

    return ciphertext

# Create a ROT-47 character list in its original order
rot47_list = [chr(i) for i in range(ord('!'), ord('~') + 1)]
# Create a ROT-47 character list in reverse order
reverse_rot47_list = rot47_list[::-1]

# Example usage:
plaintext = "EspionageCTF{r0t_c@N_b3_rEc1pROC@teD}"
encrypted_text = custom_rot47_encrypt(plaintext, rot47_list, reverse_rot47_list)
decrypted_text = custom_rot47_encrypt(encrypted_text, rot47_list, reverse_rot47_list)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
