"""
    _summary_
    Determine whether a number is odd or even,
    it's parity. This is evaluated using True or False
    
    
"""


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else: 
        print("Odd")

def is_even(n):
    return n % 2 == 0 

    # Alternate representation 
    # return True if n % 2 == 0 else False

    # OR

    # if n % 2 == 0:
    #     return True
    # else: 
    #     return False


main()