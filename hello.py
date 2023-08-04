def main():

    # prompt the user for their name    
    name = input('Enter your name: ')

    # call the hello function
    hello(name)

def hello(name):
    '''
    Prints out a greeting to the user
    '''
    print(f"Hello, {name}!")

# call the main function
main()
