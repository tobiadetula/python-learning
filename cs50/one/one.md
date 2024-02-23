#week1 #python #cs50p #conditionals

## Python File List

1. [compare.py](cs50/one/compare.py)

### Learning Achievements

#### [compare.py](cs50/one/compare.py) section

1. Using `if` statement:

``` python
#  comparing the value of x and y
if x > y :
	print(f"x is greater than y")

if x < y:
	print(f"x is less than y")

if x == y:
	print("x is equal to y")
```

The expression is referred to as a boolean expression. It is often used with [[conditionals]]. It evaluates to a `True` or `False` 

2. Using `elif` statement:

``` python
#  comparing the value of x and y
if x > y :
	print(f"x is greater than y")

elif x < y:
	print(f"x is less than y")

elif x == y:
	print("x is equal to y")
```

The expression only evaluates the next conditional only if the previous one was not `True`. The first version asks 3 questions, but only one question may be asked based on the user input.

3. Using `else` statement:
   
   ```python
#  comparing the value of x and y
if x > y :
    print(f"x is greater than y")

# will only be run if x is not greater than y
elif x < y:
    print(f"x is less than y")
    
# will only be run if x is not less than y 
else:
    print("x is equal to y")
```

Reduces the number of question asked to just 2/
### Relevant Links
- [Python Docs](https://docs.python.org)
- [Builtin String Type Modifiers](https://docs.python.org/3/library/stdtypes.html#string-methods)
