import random
import string

def generate_password(length):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))

        if length <= 0:
            print("Password length must be a positive integer.")
            return

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
