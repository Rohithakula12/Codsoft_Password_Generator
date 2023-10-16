import random
import string

def generate_password(length=12):
    # Define the character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))

    if password_length < 8:
        print("Password length should be at least 8 characters.")
    else:
        password = generate_password(password_length)
        print("Generated Password:", password)
