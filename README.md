# password generator task3
import random
import string

def generate_password(length, use_symbols=True):
    # Characters: letters + digits (+ symbols if user wants)
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("===== Welcome to Sharmaji's Password Generator =====")
    while True:
        try:
            length = int(input(" Enter desired password length: "))
            if length <= 0:
                print("Password length must be greater than 0.")
                continue

            choice = input("Include special symbols? (y/n): ").lower()
            use_symbols = True if choice == 'y' else False

            password = generate_password(length, use_symbols)
            print("Your generated password is:", password)

            # Ask if user wants another password
            again = input("🔁 Generate another password? (y/n): ").lower()
            if again != 'y':
                print("Thank you for using Sharmaji's Password Generator. Stay safe!")
                break

        except ValueError:
            print("Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
