#week1 #python #cs50p #conditionals

## Python File List

1. [compare.py](cs50/one/compare.py)
2. [equal.py](cs50/one/equal.py)
3. [grade.py](cs50/one/grade.py)

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

Reduces the number of question asked to just 2.

#### [equal.py](cs50/one/equal.py) section

4. Using `or` statement:
   
   ```python
# compares whether x is less than y OR greater than y
if x < y or x > y:
    print("x is not equal to y")    
    
# will only be run if x is not equal y 
else:
    print("x is equal to y")
```

5. Using `!=` statement:
   
   ```python
# compares whether x is not equal to  y
if x != y:
    print("x is not equal to y")    
    
# will only be run if x is not equal y 
else:
    print("x is equal to y")
```

6. Using `==` statement:
   
   ```python
# statement in reverse
# compares whether x is equal to  y
if x == y:
    print("x is equal to y")    
    
# will only be run if x is not equal y 
else:
    print("x is not equal to y")
```

#### [grade.py](cs50/one/grade.py) section

7. Using `>=` and `<=` statement:
   
   ```python
score = int(input("Score: "))

# Grade comparison calculation
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score <= 90:
    print("Grade: B")
elif score >= 70 and score <= 80:
    print("Grade: C")
elif score >= 60 and score <= 70:
    print("Grade: D")
else:
    print("Grade: F")
```

8. Combining Comparison Statements

```python 
# Grade comparison calculation
if score >= 90 and score <= 100:
    print("Grade: A")

# Alternate means of writing 
if 90 <= score and score <= 100:
    print("Grade: A")
# OR
if 90 <= score <= 100:
    print("Grade: A") 
```

9. Reducing Comparison Statement Range
   
 ```python 

if score >= 90:
    print("Grade: A")
elif  score >= 80:
    print("Grade: B")
elif  score >= 70:
    print("Grade: C")
elif  score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


```

`elif` is necessary to make the `if` statements mutually exclusive. Otherwise in this implementation all conditional will evaluate as `True` 
### Relevant Links
- [Python Docs](https://docs.python.org)
- [Builtin String Type Modifiers](https://docs.python.org/3/library/stdtypes.html#string-methods)
