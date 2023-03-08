import random
import string

def generate_password(length):
    # Define the characters to use in the password
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly selecting characters from the set
    password = ''.join(random.choice(chars) for i in range(length))
    
    return password

# Ask the user for the desired length of the password
length = int(input("Enter the length of the password: "))

# Generate and print the password
password = generate_password(length)
print("Generated password:", password)
