"""
    _summary_
    compare two user variables using or, and, &  not
    
"""



x = int(input("What's x? "))
y = int(input("What's y? "))

# compares whether x is less than y OR greater than y
if x < y or x > y:
    print("x is not equal to y")    
    
# will only be run if x is not equal y 
else:
    print("x is equal to y")