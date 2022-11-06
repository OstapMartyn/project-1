user_input = input('Please provide an integer: ')

try:
    int(user_input)
    print(f'RESULT: {user_input}')
except ValueError as error:
    print(f'ERROR: {error}\nPlease provide an integer!')