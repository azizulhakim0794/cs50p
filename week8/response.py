# python3 response.py

from validator_collection import checkers

email = input("What's your email address? ")

is_email_address = checkers.is_email(email)

if is_email_address:
    print("Valid")
else:
    print("Invalid")