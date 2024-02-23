"""_summary_
    demonstrate exception handling
"""

# Version using else 
# while True:
#     try: 
#     # Request for an Integer
#         x = int(input("What's x? "))
#     except ValueError: 
#     # Check for ValueError   
#         print("x is not an integer")
#     else:
#     # print x if there is no ValueError   
#         break        
        
# print(f"x is {x}")


while True:
    try: 
    # Request for an Integer
        x = int(input("What's x? "))
        break
    except ValueError: 
    # Check for ValueError   
        print("x is not an integer")
print(f"x is {x}")