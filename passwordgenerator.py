import random
import string


def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."


    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation


    all_chars = lowercase + uppercase + digits + symbols


    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number for length.")


if __name__ == "__main__":
    main()
