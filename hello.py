# Ask user for name, remove any leading or trailing spaces, 
# and capitalize the first letter of the first and last name...
# and then store the name in a variable called name 
name = input('Please enter your name: ').strip().title()

# Print out hello and name

# Will concat the string
# print('Hello, ' + name)

# Will print out the string using multiple arguments
# print('Hello', name, sep=', ')

# Will print out the string using format strings
print(f'Hello, {name}!')