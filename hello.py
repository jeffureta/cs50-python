# Ask user for name
name = input('Please enter your name: ')

# Strip any whitespace from the name
name = name.strip()

# Capitalize the first letter of the first and last name
name = name.title()

# Print out hello and name

# Will concat the string
# print('Hello, ' + name)

# Will print out the string using multiple arguments
# print('Hello', name, sep=', ')

# Will print out the string using format strings
print(f'Hello, {name}!')