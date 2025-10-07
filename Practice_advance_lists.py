passwords = [
    {'service': 'takeaway', 'password': 'asdf', 'added_on': '21/03/22'},
    {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
    {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
    ]

# We can do it with a for loop (version 1):
def are_all_passwords_long_enough(passwords):
    for password in passwords:
        if len(password['password']) < 8:
            return False
    return True

print(are_all_passwords_long_enough(passwords))

#We can do it using filter (version 2) 
#by searching for all the passwords that are too short 
# #and checking that the resulting list is empty:

def is_too_short(password):
    return len(password['password']) < 8

def filter_are_all_passwords_long_enough(passwords):
    return len(
        list(
            filter(
                is_too_short,
                passwords
            )
        )
    ) == 0

print(filter_are_all_passwords_long_enough(passwords))

# We can get rid of the is_too_short function 
# by using filter with a lambda (version 2.1):
def lambda_are_all_passwords_long_enough(passwords):
    return list(
        filter(
            lambda password: len(password['password']) < 8,
            passwords
        )
    ) == []

print(lambda_are_all_passwords_long_enough(passwords))

def list_comp_are_all_passwords_long_enough(passwords):
    return len(
        [
            password
            for password
            in passwords
            if len(password['password']) < 8
        ]
    ) == 0

print(list_comp_are_all_passwords_long_enough(passwords))

def when_added(date_to_find):
    return list(
        filter(
            lambda password: password['added_on'] == date_to_find,
            passwords
        )
    )

print(when_added('22/03/22'))

def whether_added(date_to_find):
    return list(
        [
            password['service'] # you can specify the Key/ value output here
            for password
            in passwords
            if password['added_on'] == date_to_find
        ]
    ) 

print(whether_added('22/03/22'))
