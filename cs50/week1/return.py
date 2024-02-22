"""_summary_
    calculator using return function 
"""


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
       
def square(of):
    value = of * of
    return value 
    
main()