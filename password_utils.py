import random
import string

def generate_password(length, upper, lower, numbers, symbols):

    characters = ""

    if upper:
        characters += string.ascii_uppercase

    if lower:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if characters == "":
        return "Select at least one option!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_strength(password):

    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if len(password) >= 12:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"
