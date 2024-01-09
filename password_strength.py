import re


def has_special_character(secret_key):
    pattern = r'[!@#$%^&*(),.?":{}|<>]'
    if re.search(pattern, secret_key):
        return True
    else:
        return False


def has_space(secret_key):
    pattern = r' '
    if re.search(pattern, secret_key):
        return True
    else:
        return False


def has_upper_case(secret_key):
    pattern = r'[A-Z]'
    if re.search(pattern, secret_key):
        return True
    else:
        return False


def is_valid_password(secret_key):
    password_length = len(secret_key)
    if password_length < 7:
        print("Password is too short")
    elif not has_upper_case(secret_key):
        print("Ad at least one uppercase letter")
    elif has_space(secret_key):
        print("Password can't have a space.")
    elif secret_key.isalpha():
        print("Add at least one number.")
    elif secret_key.isdigit():
        print("Add at least one letter.")
    # elif to check if password is missing a special character
    elif not has_special_character(secret_key):
        print("Add a special character!")
    else:
        print("Password is strong!")
        exit()


password = input("Enter your desired password: ")

while not is_valid_password(password):
    password = input("Enter your desired password: ")
