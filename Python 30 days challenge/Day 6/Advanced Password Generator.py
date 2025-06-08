import secrets
import string

def generate_password(length=8):
    if length < 4:
        raise ValueError("Minimum length is 4")

    # Required characters
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    # Fill remaining characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += [secrets.choice(all_chars) for _ in range(length - 4)]

    # Shuffle and return
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

# Example usage
print("Generate Password:", generate_password())
