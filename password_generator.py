import random 
import string 

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    char = letters 

    if numbers: 
        char += digits
    
    if special_characters:
        char += special

    password = ''
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(char)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_number

        if special_characters:
            meets_criteria = meets_criteria and has_special

    return password

password = generate_password(10)
print(password)

