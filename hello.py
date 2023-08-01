# Ask user for name
name = input('Please enter your name: ')

# Strip any whitespace from the name
name = name.strip()

# Print out hello and name

# Will concat the string
# print('Hello, ' + name)

# Will print out the string using multiple arguments
# print('Hello', name, sep=', ')

# Will print out the string using format strings
print(f'Hello World, {name}!')