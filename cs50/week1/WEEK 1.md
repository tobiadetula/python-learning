#week1 #python #cs50p
## Python File List

1. [[hello.py]] - to ask a user for their name
2. [[calculator.py]] - demonstrating type conversions and mathematical functions
3. [[function.py]] - to use a function to print hello

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
15. Type Conversion
```python 
x = int() # convert to integer 
x = float() # convert to float 
```
16.  Variable Rounding 
```python 
# round(value, number of decimal places)
z = round(x + y, 2)
```
17.  Value Separator
```python 
# Outputs sum of x and y, Ex: 20 + 980 = 1,000 with seperator
# format string required 
print(f"{z:,}")
```
18.  Alternate fstring rounding method 
```python
# Outputs z with float values rounded to 2 decimal places, alternate of round function()
print(f"{z:.2f}")
```

#### [[function.py]] section
19.  Function  Definition 
```python
def hello():
# def - used to indicate function definition 
# hello() - function name 
# : colon - represents stay tuned for indentation.
# anything indentented under colon is part of the function
```
20.  Function with Argument
```python
def hello(to):
	print("hello,", to)

# expected function parameter to 
hello(name)
# variable name is copied over to 'to'; name = to
```
21.  Function Argument with Default Value
```python 
def hello(to="world"):
	print("hello,", to)

# expected function parameter to 
hello()
# output to terminal: hello, world
```
22.  Main Function Definition 
```python
# Allows function to be ordered in any manner either hello before main or main before hello
def main():
	name = input("What's your name? ").strip().title()
	hello(name)
	
def hello(to="world"):
	print(f"hello, {to}")

# Calls the main function
main()
# Script does not run unless the function is called 
```
23. Function Scope 
```python
# Allows function to be ordered in any manner either hello before main or main before hello
def main():
	name = input("What's your name? ").strip().title()
	hello()
	
def hello(to="world"):
	print(f"hello, {name}")

# Calls the main function
main()
# Script does not run unless the function is called 
```
24. 

### Video Links
- [CS50P - Lecture 0 - Functions, Variables](https://www.youtube.com/watch?v=JP7ITIXGpHk&t=842s)
- [Python Docs](https://docs.python.org)
- [Builtin String Type Modifiers](https://docs.python.org/3/library/stdtypes.html#string-methods)
- 

