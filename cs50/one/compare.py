"""
    _summary_
    compare two user variables 
    
"""



x = int(input("What's x? "))
y = int(input("What's y? "))

#  comparing the value of x and y
if x > y :
    print(f"x is greater than y")

# will only be run if x is not greater than y
elif x < y:
    print(f"x is less than y")
    
# will only be run if x is not less than y 
elif x == y:
    print("x is equal to y")