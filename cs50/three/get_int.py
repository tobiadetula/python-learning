"""_summary_
    demonstrate exception handling in a function
"""

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")



# Using break to exit the loop
# def get_int():
#     while True:
#         try: 
#         # Request for an Integer
#             x = int(input("What's x? "))
#         except ValueError: 
#         # Check for ValueError   
#             print("x is not an integer")
#         else:
#         # exit the loop if there is no ValueError   
#             break        
#     return x

# Using return to exit the loop
# def get_int():
#     while True:
#         try: 
#         # Request for an Integer
#             x = int(input("What's x? "))
#         except ValueError: 
#         # Check for ValueError   
#             print("x is not an integer")
#         else:    
#             return x

# Without using the else statement
def get_int(prompt):
    while True:
        try: 
            return int(input(prompt))
        except ValueError: 
        # Check for ValueError   
            # print("x is not an integer") # Print a warning
            pass # go through the loop again without taking any action 

main()