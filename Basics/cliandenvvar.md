### Command Line Arguments
--------------------------

* In Python allow a user to provide input to a Python script 
when it is executed from the command line. This is useful for passing options, filenames, or parameters to scripts at runtime.

* In Python, command line arguments are stored in the `sys.argv` list, provided by the `sys` module.
Using sys.argv
The sys.argv list contains the arguments passed to the script:
  * `sys.argv[0]` is the name of the script itself.
  * `sys.argv[1]`, `sys.argv[2]`, etc., represent the arguments passed to the script.

Example:

```python 

import sys

def add(num1,num2):
    add = num1 + num2
    return add

def sub(num1,num2):
    sub = num1 - num2
    return sub

def mul(num1,num2):
    mul = num1 * num2
    return mul

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    output = add(num1,num2)
    print(output)

elif operation == "sub":
    output = sub(num1,num2)
    print(output)

elif operation == "mul":
    output = mul(num1,num2)
    print(output)
```

### Environment Variables

* Environment variables are dynamic variables maintained by the  operating system that can affect the way running processes behave. They are often used for configuration settings, like database credentials, API keys, or system paths, and provide a way to pass
information into a program without hardcoding it.

* In Python, environment variables can be accessed using the os module.
* You can use the os.environ dictionary to access environment variables.
  
Example:
Defining the Environment variables like
set password=”anitha”
in Python program:
import os
print(os.getenv("password"))



