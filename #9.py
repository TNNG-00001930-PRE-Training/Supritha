#9
import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

passwords = input("Enter comma-separated passwords: ").split(',')

valid_passwords = [password for password in passwords if is_valid_password(password)]

print(','.join(valid_passwords))
