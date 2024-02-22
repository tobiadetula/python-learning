"""_summary_
    calculator using return function 
"""


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
       
       
# return the square of the n value       
def square(n):
    # return n * n
    # Alternate square of a number definition
    # return n ** 2 
    # Alternate power of a number definition
    return pow(n,2)
     
    
main()