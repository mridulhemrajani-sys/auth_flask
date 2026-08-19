import bcrypt
import re

def generate_hash_password(password):
    password_bytes=password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    # print(hashed_password)
    return hashed_password.decode('utf-8')

# print(generate_hash_password('123456'))

def verify_password(password, hashed_password):
    password_bytes = password.encode('utf-8')
    hashed_password=hashed_password.encode('utf-8')
    print(password_bytes)
    return bcrypt.checkpw(password_bytes, hashed_password)

def is_valid_email(email):
    EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.fullmatch(EMAIL_REGEX,email):
        return True
    return False
