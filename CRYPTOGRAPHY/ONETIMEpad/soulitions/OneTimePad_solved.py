# Michael N || Mm0
#Issession CTF 2024 Challenge --> Cryptogarphy --> ONE-Time Pad 
import string


class challenge: 
        
        def __init__(self, message_txt, key_txt, message_num, key_num):
            self.message_txt = message_txt
            self.key_txt = key_txt
            self.message_num = message_num
            self.key_num = key_num

        def ENCRYPTED(self):
            print(" FORMULA [ ENCRYPT =  (MESSAGE + KEY) MOD 26 ] ") # formula OUT PUT 
            encrypted_msgNum = [(m + k) % 26 for m, k in zip(self.message_num, self.key_num)] #  grouping my two lists with zip and tuples....
            print(f"Encrypted msg = {encrypted_msgNum}") #this is what the user is provided with and the must try to reverse engineer the encryption process 
            return encrypted_msgNum
        
        def DECRYPT(self, encrypted_msg_num):
            print(" FORMULA [ ENCRYPT =  (MESSAGE - KEY) MOD 26 ] ") # formula OUT PUT 
            decrypted_msg = []
            decrypted_msg_num = [(e - k) % 26 for e, k in zip(encrypted_msg_num, self.key_num)]
            print(f" decrypted msg num = {decrypted_msg_num}") 

            ALPHABET_LST = list(string.ascii_lowercase) # list of all the letter in the alphabet 
            for i in decrypted_msg_num:
                i = i - 1
                # Ensure the index is within the valid range (0 to 25)
                i %= 26
                decrypted_msg.append(ALPHABET_LST[i])
            print(f"Plain Text MSG = {decrypted_msg}") #printing msg in plain text
            print(r"FLAG =  EspionageCTF{ONETIMEPAD}") #raw str output of the flag 

        """def output(self):
            print(f"encrypted Message (Numeric Indices): {self.message_num}")
            print(f"rypted Message: {self.}")
            print(f"Decrypted Message: (Numeric Indices): {decrypted_msg_num}")
            print(f"Decrypted Message: {decrypted_msg}")"""
        

def main(): 
    print('-- MAIN --') # str for main 

    

    ### testing below ###
    testing = challenge(
        message_txt = "ONETIMEPAD", #plain text version of the msg aka THE FLAG...
        key_txt = "MTWENTYSIX", #plain text of the key (This will be provide to the user in the form of a morse code audio file the must listen or use a morse code translator to translate the key)
        message_num = [ 15, 14, 5, 20, 9, 13, 5, 16, 1, 4], #this is the number index of each letter in the alphabet that corresponds to each char within the msg
        key_num = [ 13, 20, 23, 5, 14, 20, 25, 19, 9, 24] # same thing but for the key 
    ) # instance i 

    encrypted = testing.ENCRYPTED() #testing output... 
    testing.DECRYPT(encrypted) # testing the decryption process which is just reversing the encryption... 


if __name__ == '__main__':
    #** Issession CTF 2024 Challenge --> Cryptogarphy --> ONE-Time Pad ** 
    
    main() # running main 