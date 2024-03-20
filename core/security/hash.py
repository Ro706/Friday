# random hash Generator : this code will genrate a random hash key
from cryptography import fernet
key = fernet.Fernet.generate_key()
print(key)

