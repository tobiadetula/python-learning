#week3 #python #cs50p #exceptions
# Exceptions
## Python File List

1. [number.py](obsidian://open?vault=python-learning&file=cs50%2Fthree%2Fnumber.py)

### Learning Achievements

#### [number.py](cs50/three/number.py) section

1. **Using `Exception Handling` statement:**

``` python
try: 
 # Request for an Integer
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError: 
 # In the case of erroneous input print the warning below
    print("x is not an integer")
```

It is best practice to only try the lines of code where you are expecting an error.  The `print` function in this case cannot give us a `ValueError`. We should move the print out of the `try` block.

```python 
try: 
 # Request for an Integer
    x = int(input("What's x? "))
except ValueError: 
    print("x is not an integer")
    
    
print(f"x is {x}")

```

This causes a `NameError` due to the [[order of operations]].  The definition of `x` fails due to `ValueError`. The `int` function raises a `ValueError` as it cannot convert `cat` to an `int`.
This prevents the assignment of  the `x` variable. 

```bash
What's x? cat
x is not an integer
Traceback (most recent call last):
  File "~/Documents/python-learning/cs50/three/number.py", line 12, in <module>
    print(f"x is {x}")
                  ^
NameError: name 'x' is not defined
```

To resolve this an  `else` statement can be used to only `print` the output in the event an `error` is not encountered.

```python 
try: 
 # Request for an Integer
    x = int(input("What's x? "))
except ValueError: 
 # Check for ValueError   
    print("x is not an integer")
else:
 # print x if there is no ValueError   
    print(f"x is {x}")
```

2. **Looping `Exception Handling`**
   Instead of having the code fail, if the user gives the wrong input we can use a loop to keep trying until we get the right input from the user.

```python 
while True:
    try: 
    # Request for an Integer
        x = int(input("What's x? "))
    except ValueError: 
    # Check for ValueError   
        print("x is not an integer")
    else:
    # print x if there is no ValueError   
        break        
        
print(f"x is {x}")
```

`break` is necessary to break out of the loop if the user inputs the correct variable. 
Example in shell is shown below:

```shell 
> python3 number.py

What's x? dsfsd
x is not an integer

What's x? sdfsd
x is not an integer

What's x? sdfsd
x is not an integer

What's x? 123
x is 123

```

The code can be shortened to: 
```python 
while True:
    try: 
    # Request for an Integer
        x = int(input("What's x? "))
        break
    except ValueError: 
    # Check for ValueError   
        print("x is not an integer")
print(f"x is {x}")
```

Using the else block helps reduce the lines of code we want to try.

3. **Function `Exception Handling` with a Loop**
   The function below can be called to request the user for an int repeatedly.
```python
def get_int():
    while True:
        try: 
        # Request for an Integer
            x = int(input("What's x? "))
        except ValueError: 
        # Check for ValueError   
            print("x is not an integer")
        else:
        # print x if there is no ValueError   
            break        
    return x
```
The `return` statement can be used similarly to the `break` statement. It can be used to `return` a value while breaking out of a loop at the same time.  
```python 
def get_int():
    while True:
        try: 
        # Request for an Integer
            x = int(input("What's x? "))
        except ValueError: 
        # Check for ValueError   
            print("x is not an integer")
        else:    
            return x
```
It can be shortened even further by moving the `return` to the `try` block and moving the `int` request to the return statement. 

***Note:*** 
		1. Variables that will not be used can be moved to the `return` statement 
		2. `try` and `except` are statements and not functions

```python 
# Without using the else statement
def get_int():
    while True:
        try: 
            return int(input("What's x? "))
        except ValueError: 
        # Check for ValueError   
            print("x is not an integer")
```

4. Ignoring an Exception with `pass`

```python
# Without using the else statement
def get_int():
    while True:
        try: 
            return int(input("What's x? "))
        except ValueError: 
        # Check for ValueError   
            pass # go through the loop again without taking any action 
   
```

5. Function Terminology
   > `Caller` - The function calling another function
   > `Callee` - The function being called
   > `Call`     - To request to use a function 
   
6. Making functions more reusable
```python 

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
    
# Without using the else statement
def get_int(prompt):
    while True:
        try: 
            return int(input(prompt))
        except ValueError: 
        # Check for ValueError   
            pass # go through the loop again without taking any action 

main()

```

7. Raising exceptions using the `raise` keyword
   
   
   
   ### Relevant Links
- [Lecture 3 - Exceptions](https://www.youtube.com/watch?v=LW7g1169v7w&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=5)