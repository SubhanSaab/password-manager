import secrets 
import string
import json

def generate_password(length, use_symbols, use_numbers):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    
    if use_symbols:
        characters += string.punctuation
    
    password = ""
    for i in range(length):
        password += secrets.choice(characters)

    return password

result = generate_password(length=16, use_symbols=True, use_numbers=False)
print(result)