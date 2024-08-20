from cryptography.fernet import Fernet

# The following block of code to generate a key is commented out since you mentioned it's in another file.

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

write_key()
