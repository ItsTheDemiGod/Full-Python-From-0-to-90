# In Python, we have a Library called cryptography which is used for Encryption
# Fernet is the module used to generate key here

from cryptography.fernet import Fernet

key =Fernet.generate_key()
cipher= Fernet(key) # here cypher is the key which we are using to encode and decode
print(key)

text = "Hello World!"
encrypted_text = cipher.encrypt(text.encode())
print(encrypted_text)


decrypt = cipher.decrypt(encrypted_text.decode())
print(decrypt)