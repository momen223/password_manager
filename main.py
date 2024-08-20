from cryptography.fernet import Fernet

# The following block of code to generate a key 
'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

write_key()
'''

def load_key():
    with open('key.key', 'rb') as file:
        key = file.read()
    return key

key = load_key()
fer = Fernet(key)

def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
    except FileNotFoundError:
        print("No passwords saved yet.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add():
    user_name = input('Enter your name please: ')
    pwd = input('Enter your password: ')
    with open('passwords.txt', 'a') as f:
        f.write(user_name + '|' + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input('Would you like to add a new password or view the passwords? Choose (add/view) or q to quit: ').lower()

    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
