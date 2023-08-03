# get two numbers from the user
# and convert them to floats 
x = float(input('Enter a number: '))
y = float(input('Enter another number: '))

# round the sum of x and y to the nearest integer
z = round(x + y)

# print out the sum of x and y with a comma for a thousands separator
print(f'{z:,}')