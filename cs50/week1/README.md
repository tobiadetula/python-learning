#week1 #python 
## Python File List

1. [[hello.py]] - to ask a user for their name
2. [[calculator.py]] - demonstrating type conversions and mathematical functions

### Learning Achievements

#### [[hello.py]] section

1. Using Comments

``` python
# - Single Line Comment
"""
"""  Multiline Comment
```

2. Token Types

``` python
	name # variable 
	print() # function 
	input() # function
```
3.  Special Functions 

``` python
	print() # print a string to terminal 
	input() # input a value to a program
```

4.  String Concatenation

``` python
	# Use the '+' symbol to concatenate a string 
	print("hello" + ", world")
	#Output: hello, world
```

5. Variable Assignment 

``` python
	name = "Variable Content"
```

6.  Python Documentation for [Print Function](https://docs.python.org/3/library/functions.html#print)

``` python
print(*objects, sep=' ', end='\n', file=None, flush=False)
#Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.

#sep - is used as a seperator. reason why by default they are seperated by a single space 
#end - how the function stream is terminated
#'\n' - new line escape sequence
```

7.  Overriding Print Default Value
```python 
print("hello, ", end="")
# Print specified to work without new line character
```

8. Positional and Named Parameters
```python 
print("hello, ", world, end = "")
# world - postional parameters
# end - named parameters
```
9.  Using backslash escape character
```python 
print("hello, \'world\'")
# prints - hello, 'world'. to terminal 
# escape character use - \'
```
10.  Using format strings 
```python
name = "David"
print(f"hello, {name}")
# prints - hello, David
```

11.  Builtin Type Options
```python 
# Removes whitespace from string 
name.strip()
# Capitalze the first letter of a string 
name.capitalize()
# Capitalize the first letter of a string after a whitespace character 
name.title()
```
	
12.  Concatenating Functions 
```python 
# Remove Whitespace and Capitalize 
name = name.strip().title()
```
13.  Splitting Strings
```python
# Split user's name into first name and last name 
first , last = name.split(" ")

```

#### [[calculator.py]] section
14.  Function Nesting 
```python 
x = int(input("What's x? "))
# input returns a string 
# int takes the return value of input and converts it to an integer
```
15. 

### Video Links
- [CS50P - Lecture 0 - Functions, Variables](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=842s)
- [Python Docs](https://docs.python.org)
- [Builtin String Type Modifiers](https://docs.python.org/3/library/stdtypes.html#string-methods)
- 

