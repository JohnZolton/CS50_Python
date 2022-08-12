# prompt a user for an email address
# and print valid or invalid
# WITHOUT using regular expressions

from validator_collection import checkers

email_address = checkers.is_email(input('Email: '))
if email_address:
    print('Valid')
else:
    print('Invalid')
