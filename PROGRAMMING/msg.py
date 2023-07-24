#text file with the encrpyted msg 


class private_msg(): #creating a class with the plain text message plus a decryption process plus the decryption key that will be stored on a server that the users will not be able to access or see 
    def __init__(self) -> None:
        super().__init__() #incase there is issue with class 
        self.__private_msg = "private msg!" #private msg in plain text in private var 
        self.__decryptiong_key = "decryption key" #decryption key in private varible 
    
    def returnMSG(self):
        return self.__private_msg # returning the message 
    
if __name__ == '__main__':
    print('!! MAIN !!') #telll me we in the MIAN NINAIN !
    testing = msg()
    #print(testing.__private_msg) #promblem this will give error = AttributeError: 'msg' object has no attribute '__private_msg'. Did you mean: '_msg__private_msg'? <-- basically defeating challenge by cheating 
    a = testing.returnMSG()
    