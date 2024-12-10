import random
import string


def generate_password():
    while True:
        password_length = int(input("Enter password length: "))
        if password_length < 8:
            print("Password length should be at least 8 characters")
            continue

        lowercase = input("Include lowercase letters? (y/n): ")
        uppercase = input("Include uppercase letters? (y/n): ")
        digits = input("Include numbers? (y/n): ")
        symbols = input("Include symbols? (y/n): ")

        password_components = ""
        if lowercase == 'y':
            password_components += string.ascii_lowercase
        if uppercase == 'y':
            password_components += string.ascii_uppercase
        if digits == 'y':
            password_components += string.digits
        if symbols == 'y':
            password_components += string.punctuation

        if not password_components:
            print("You must select at least one character type (letters, numbers, symbols).")
            continue

        password = ''.join(random.choice(password_components) for _ in range(password_length))
        print("\nYour generated password is:", password)

        generate_more = input("\nWould you like to generate another password? (y/n): ")
        if generate_more.lower() != 'y':
            break


if __name__ == "__main__":
    generate_password()