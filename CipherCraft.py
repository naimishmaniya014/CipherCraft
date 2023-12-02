import random
import string

def generate_password(length, complexity):
    characters = {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase,
        'digits': string.digits,
        'special': string.punctuation
    }

    # Create a list of character sets based on complexity chosen by the user
    character_set = [characters[ctype] for ctype in complexity]

    # Flatten the character_set list
    all_characters = ''.join(character_set)

    # Ensure the length of the password is at least 4 characters
    length = max(length, 4)

    # Generate the password
    password = ''.join(random.sample(all_characters, length))
    return password

def main():
    print("Welcome to the Secure Password Generator!")
    print("---------------------------------------")

    while True:
        try:
            length = int(input("Enter the length of the password: "))
            complexity = input("Enter the complexity (lowercase, uppercase, digits, special), separated by commas: ").split(',')

            password = generate_password(length, complexity)
            print("Generated Password:", password)
            break
        except ValueError:
            print("Please enter a valid length for the password.")

if __name__ == "__main__":
    main()