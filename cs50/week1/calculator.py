"""_summary_
    requests for user input as string, the converts to int 
    and performs addition 
"""
# # Integer Definitions Demonstration
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# Float Definitions Demonstration
x = float(input("What's x? "))
y = float(input("What's y? "))

# Variable addition 
# z = int(x) + int(y) // Alternate version
z = round(x + y,2) 

# Printing output to terminal 
# print(z) - Outputs sum of x and y, Ex: 20 + 980 = 1000

# Outputs sum of x and y, Ex: 20 + 980 = 1,000 with seperator
print(f"{z:,}")