import random
import string
# Function to generate a strong password
def generate_password(length):
    # Define the character sets for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password using the specified length
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password
# Main program
def password_generator():
    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("Password should be at least 8 characters long for security.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    # Generate the password
    password = generate_password(length)
    # Display the generated password
    print(f"Your generated password is: {password}")
# Run the password generator
password_generator()
