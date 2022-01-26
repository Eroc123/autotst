import base64
from cryptography.fernet import Fernet
from getpass import getpass
key = Fernet.generate_key()
fernet = Fernet(key)
print('Please enter infomation according to the TST website')
email = input('Email : ').encode()
password = getpass(stream = '*').encode()

email = fernet.encrypt(email)
password = fernet.encrypt(password)
  
# opening the file in write mode and 
# writing the encrypted data
with open('PASSWORD', 'wb') as encrypted_file:
    encrypted_file.write(password)
with open('EMAIL', 'wb') as encrypted_file:
    encrypted_file.write(email)
with open('KEY', 'wb') as encrypted_file:
    encrypted_file.write(key)
print('Finished setting up')
