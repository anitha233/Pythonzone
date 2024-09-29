### Conditional Handling

* In Python, we use `if`,`elif` or `else if` and `else` to create a conditional statements.

## If statement
* The `if` statement is used to execute the block the code if a specific condition is `True`. If condition is `False` then code is skipped.

syntax:
```python
if condition:
    # code to execute if the condition is True
```   

## Example

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

## elif statement

* The `elif` statement allows you to check additional conditions if the previous `if` and `elif` conditions are False.can have multiple `elif` statements after the initial `if` staement.

Syntax:

```python
if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition2 is True
elif condition2:
    # code to execute if condition3 is True
else:
    # code to execute if none of the conditions are True 
```
## Example

```python
x = 10
if x > 15:
  print("x is greater than 15")
elif x > 5:
  print("x is greater than 5 but not greater than 15")
else:
  print("x is not greater than 5")
```

## else statement

* Used to execute when none of the previous conditions(`if` or `elif` statements) are True.
  
syntax:
```python
if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False
```

## Example

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```    


 