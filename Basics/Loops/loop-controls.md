* In Python, there are two primary loop control statements are "break" and "continue"

## break statement
* Used to exit the loop immediately.It can be applied for both the "for" and "while" loop allows to terminate the loop,when the condition is met.

Example:
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)
```

## continue statement

* Used to skip the current iteration and continue the next step.

Example:
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)
``` 
  
