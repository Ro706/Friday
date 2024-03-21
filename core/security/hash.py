# random hash Generator : this code will genrate a random hash key
from cryptography import fernet # pip install cryptography : this library is used to generate a random hash key
key = fernet.Fernet.generate_key() # here we are generating a random hash key
print(key)  # printing the hash key

