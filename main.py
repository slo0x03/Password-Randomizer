import string as s
import secrets

def generate_password(length: int, symbols: bool, uppercase: bool):
    combination = s.ascii_uppercase + s.digits

    if symbols:
        combination += s.punctuation

    if uppercase:
        combination += s.ascii_uppercase

        combination_length = len(combination)

        new_password = ""

        for _ in range(length):
            new_password += combination[secrets.randbelow(combination_length)]

        return new_password



for _, index in enumerate(range(5)):
    password = generate_password(length=35, symbols=True, uppercase=True) #symbol and uppercase both set to true by default, can be changed to exclude them, can also change length (would not go below 15 or above 35)
    print(index + 1, ">>", password)
