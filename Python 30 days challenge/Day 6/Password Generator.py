
# random and secrets are both used for password generation,
#     but secrets is more secure and recommended for sensitive applications.

import random
import secrets
import string

def password_with_secrets(length=8):
    all_chars = string.ascii_letters + string.digits +string.punctuation
    return "".join(secrets.choice(all_chars) for _ in range(length))

def password_with_random(length=8):
    all_chars = string.ascii_letters + string.digits +string.punctuation
    return "".join(random.choices(all_chars,k=length))

print("Random Password: ", password_with_random())
print("Secrets_password: ", password_with_secrets())