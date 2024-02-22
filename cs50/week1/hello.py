"""

Ask a user for their name, demonstrating the use of input and print functions

""" 
 
# Print a string to Terminal and recieve user input
name = input("What's your name? ")
# Strip the whitespace from string and store the altered version in the same variable
name = name.strip() 
# Capitalize user's name 
# name = name.capitalize() # only name before whitespace
name = name.title()


# Print user name to terminal after storing in variable name 
print("Hello,",name) # Print a String to Terminal

# Add a seperate section asking for last name and demonstrating print function override
# Then remove whitespace from title
# Then capitalize user's title

title = input("and your title ").strip().capitalize()
# title = title.strip() 
# title = title.capitalize() 

# Print function overrides using named Parameters
print("Nice to meet you, ",title,end =". ")
print(name)

