def main():
    # prompt the user for their name    
    name = input('Enter your name: ')

    # call the hello function
    hello(name)

def hello(to='World'):
    '''
    Prints out a greeting to the user.
    if no name is provided, or the name is an empty string, it will print hello, World!
    '''
    if to == '':
        to = 'World'
    print(f"Hello, {to}!")

# call the main function
main()

