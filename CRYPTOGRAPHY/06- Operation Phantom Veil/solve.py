def encrypt(original_text):
    #ROT47 original list
    original_list = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    
    #ROT47 reverse list
    reverse_list = "~}|{zyxwvutsrqponmlkjihgfedcba`_^]\\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)('&%$#\"!"

    encrypted_text = ""
    for i, char in enumerate(original_text):
        if i % 2 == 0:
            # Encrypt using ROT47 in original order
            if char in original_list:
                char_index = original_list.index(char)
                encrypted_char = original_list[(char_index + 47) % 94]
            #else:
             #   encrypted_char = char
        else:
            # Encrypt using ROT47 in reverse order
            if char in reverse_list:
                char_index = reverse_list.index(char)
                encrypted_char = reverse_list[(char_index + 47) % 94]
            #else:
             #   encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text


original_text = "EspionageCTF{r0t_c@N_b3_rEc1pROC@teD}"
encrypted_text = encrypt(original_text)
print("Original text:", original_text)
print("Encrypted text:", encrypted_text)
decrypted_text = encrypt(encrypted_text)
print("Decrypted Text:", decrypted_text)
