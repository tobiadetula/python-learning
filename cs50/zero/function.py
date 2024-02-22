
"""_summary_
   demonstrates function definition and 
   default argument passing
"""



def main():
    # function without argument passed 
    # hello()
    
    # Print a string to Terminal and receive user input
    name = input("What's your name? ").strip()
    
    # function with argument passed
    hello(name)

def hello(to="world"):
	print(f"hello, {to}")

# Calls the main function
main()