# validating user input - its small game where we accept only certain inputs
# from the user

# validate user input
# 1. username is no more than 12 characters
# 2. username must not contain digits
# 3. username must not contain spaces


username = input('Enter your name: ')

if len(username) > 12 :
    print(" the username is too long")
    username = input('Enter your name: ')
elif username == " " :
    print('your username shoould not hold any spaces')
    username = input('Enter your name: ')
elif username.isalnum() == True :
    print('your username is alphanumeric')
    username = input('Enter your name: ')
else:
    print(f'your username is {username}')



