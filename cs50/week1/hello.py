"""

Ask a user for their name, demonstrating the use of input and print functions

""" 
 
firstName = input("What's your name? ") # Print a string to Terminal and recieve user input
firstName = firstName.strip() # Strip the whitespace from string and store the altered version in the same variable

# Print user name to terminal after storing in variable name 
print("Hello,",firstName) # Print a String to Terminal

# Add a seperate section asking for last name and demonstrating print function override
lastName = input("and your last name? ")

# Print function overrides using named Parameters
print("Nice to meet you, ", firstName ,end ="")
print(lastName)

