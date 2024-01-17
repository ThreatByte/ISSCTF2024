import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
import hashlib
import subprocess
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import os
from datetime import datetime
import pefile

def calculate_md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

class CTFChallenge(QWidget):
    def __init__(self):
        self.final_password = "Str34mC1ph3r_0v3rl04d"
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ISSessions 2024 CTF')

        self.resize(400, 100)

        self.serialNumberInput = QLineEdit(self)
        self.validateButton = QPushButton('Validate', self)
        self.validateButton.clicked.connect(self.validateSerial)
        self.resultLabel = QLabel('', self)


        self.passwordInput = QLineEdit(self)
        self.passwordInput.setEchoMode(QLineEdit.Password)  # Hide password input
        self.passwordInput.hide()  # Hide it initially

        self.serialLabel = QLabel('Enter Serial Number:', self)


        self.passwordLabel = QLabel('Enter Password:', self)
        self.passwordLabel.hide()  # Initially hide the label
        

        layout = QVBoxLayout(self)
        layout.addWidget(self.serialLabel)
        layout.addWidget(self.serialNumberInput)
        
        
        
        layout.addWidget(self.resultLabel)
        
        layout.addWidget(self.passwordLabel)
        layout.addWidget(self.passwordInput)
        layout.addWidget(self.validateButton)

    def is_valid_pe_file(self, file_path):
        try:
            pe = pefile.PE(file_path)
            return True  # The file is a valid PE file
        except:
            return False  # The file is not a valid PE file

    def validateSerial(self):
        serial = self.serialNumberInput.text()
        current_year = str(datetime.now().year)
        md5_hash = calculate_md5('2C3D4E5F.DAT')
        # Serial number format validation
        if serial.startswith(current_year) and serial[len(current_year)+1:len(current_year)+33] == md5_hash:
            self.resultLabel.setText('Serial number is valid!')
            self.passwordLabel.show()
            self.passwordInput.show()  # Show the password input field
            self.validateButton.clicked.disconnect()  # Disconnect existing slot
            self.validateButton.clicked.connect(self.validatePassword) 
        else:
            self.resultLabel.setText('Invalid serial number.')
    
    def validatePassword(self):
        
        if self.passwordInput.text() == self.final_password:
            self.resultLabel.setText('Password is valid!')
            self.decrypt_file()
        else:
            self.resultLabel.setText('Invalid password.')

    def decrypt_file(self):
        file_path = "B2C3D4E5.DAT"
        password = self.final_password
        decrypted_file_path = "QDecryptor.exe"
        with open(file_path, 'rb') as file:
            salt = file.read(16)
            iv = file.read(16)
            encrypted_data = file.read()

        key = PBKDF2(password, salt, dkLen=32)
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        decrypted_data = cipher.decrypt(encrypted_data)

        pad = decrypted_data[-1]
        decrypted_data = decrypted_data[:-pad]
        
        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted_data)
        
        if self.is_valid_pe_file(decrypted_file_path):
            self.resultLabel.setText('Decryption and execution completed.\nLoader has been saved.')
        else:
            self.resultLabel.setText('Invalid executable file.')

        self.resultLabel.setText('Decryption and execution completed.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CTFChallenge()
    ex.show()
    sys.exit(app.exec_())
