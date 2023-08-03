# get two numbers from the user
# and convert them to floats 
x = float(input('Enter a number: '))
y = float(input('Enter another number: '))

# round the sum of x and y to the nearest integer
z = round(x + y)

# print out the equation using format strings
print(f'{x} + {y} = {z}')