### Tuples

* Tuples are immutable,their contents cannot be changed after creation.Tuples are used for grouping related data.

## Creating Tuple

* In Python,create a tuple using parentheses()
```python
my_tuple = (1,2,'apple','banana')
```

## Tuple indexing

* Tuple elements are indexed, starting from zero for the first element.
```python
first_element = my_tuple[0] # Access the first element
```

## Tuple length

* find the length of a tuple using len() function
```python
tuple_length = len(my_tuple) # length of tuple is 4
```

## Accesing tuple elements

* Tuples are immutable, you can access only their elements
```python
second_element = my_tuple[1] # Access the second element
```

## Pack and Unpack the Tuple

* you can pack multiple values into a tuple,and unpack them into separate variables.
  
```python
coordinates = (3,4)
x , y = coordinates # Unpack the tuple into x and y (x=3,y=4)
```

## Concatinating Tuples

* concatenate two or more tuples to create a new tuple
```python
new_tuple = my_tuple + (3.14,'kiwi') #concatenates my_tuple with new tuple
```

## Checking for an element

* check if an element exists in a tuple, using `in` keyword
```python
is_present = 'apple' in my_tuple # checks if apple is present in the tuple
```

## Using tuples for multiple return values

* Tuples are often used to return multiple values from functions
```python
def get_coordinates():
    return (3, 4)

x, y = get_coordinates()  # Unpack the returned tuple (x=3, y=4)
```

## Differences between list and tuple

# List

* Mutability - Lists are mutable,their elements can be added, removed or modified after the creation.Methods like append(),remove(),pop() to change the contents of list.
* Syntax - Lists are created using square brackets[ ],elements are separated by commas.
Example:
```python
my_list = [1, 2, 3, 'apple', 'banana']
```
* Performance - Lists have slower performance compared to tuples because they are mutable,modifying a list requires memory reallocation which is slower for large lists. 
* Usecases - Lists are used when you need a collection of elements that can change,dynamic list of items or data that can be modified.
* Iteration - Use for loop or other iteration methods to iterate over the elements of a list.
Example:
```python
for item in my_list:
    # Process each item
```    
* Memory Usage - Lists generally consume more memory than tuples because they need to store additional info to support mutability.

## Tuple

* Mutability - Tuples are immutable, once they are created,their elements cannot be changed,add or modify.
* Syntax - Tuples are created using parenheses ().Elements are separated by commas.
Example:
```python
my_tuple = (1, 2, 'apple', 'banana')
```
* Performance - Tuples have better performance,especially for read-only operations because of their immutablility,they do not require memory reallocation.
* Usecase - Tuples are used when you need an ordered collection of elements that should not be changed like representing a point in 2D space(x,y).
* Iteration - Use for loop for iterate over the elements.
Example:
```python
for item in my_tuple:
    # Process each item
```
* Memory Usage - Tuples consume less memory because they are immutable.  


  