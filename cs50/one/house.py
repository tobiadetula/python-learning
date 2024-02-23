"""
    _summary_
    Using the match  
"""

name = input("What's your name? ").strip().lower()

if name == "harry" or name == "hermione" or  name == "ron" :
    print("Gryffindor")
        
elif name == "draco":
    print ("Slytherin")
    
else:
    print ("Who?")