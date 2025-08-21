import string
import secrets

char_sets = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "digits": string.digits,
    "symbols": string.punctuation
}

print('Password generator')
size = int(input('Enter password size: '))

all_chars = ""
for name, chars in char_sets.items():
    choice = input(f"Include {name}? (y/n): ").strip().lower()
    if choice == "y":
        all_chars += chars

if not all_chars:
    print("No character sets selected! Exiting...")
else:
    password = "".join(secrets.choice(all_chars) for _ in range(size))
    print("Generated password:", password)