# python_code_wars
### How to Python3

The following are notes taken for code wars problem sets in python

#### How do I get started with Python3?
``` python
# First download python3
# How to access python 3 on the command line?
python3
# How to run a python file?
python3 filename.py
# How to install a module?
pip3 install module_name
```

#### Zen of Python
```
Big Ideas with Little Code
Significant whitespace
  Indent 4 spaces... eww!
  No curly braces... Yes!
  ... acceptable tradeoff
```
#### How to print to console:
```python
print('Hello World!')
```

#### How to assign a variable:
```python
x = 1
y = 2
x + y == 3
# True
```

#### How to make function:
```python
def myFunc:
```

#### How to if else:
```python
if expression:
    return true
else:
    return false
```

#### How to else if:
```python
elif a > b:
```

#### How to for loop:
```python
# works like forEach method
# iterates over elems not the index
for x in list:
```

#### How to turn string into array:
```python
string = 'the brown cow'
arrToStr = string.split()
# ['the', 'brown', 'cow']
arrToStr = string.split(' ')
# same as above
arrToStr = string.split(' ')
# ['the br', 'wn c', 'w']
```

#### How to split string into array of characters?
```python
string = 'the brown cow'
arrToStr = list(string)
# ['t', 'h', 'e', ' ', 'b', 'r', 'o', 'w', 'n', ' ', 'c', 'o', 'w']
# string.split('') will throw an error
```

#### How to instantiate null var:
```python
value = None
```

#### How to increment a number:
```python
num += 1
# num++ is invalid
```

#### How to lower case a string:
```python
string.lower()
```

#### To count the number of times a character appears in a string:
```python
string.count('x') #outputs count of 'x'
```

#### Find max / min length string in array:
```python
max(len(x) for x in ['the', 'brown', 'cow']) # outputs 5
min(len(x) for x in ['the', 'brown', 'cow']) # outputs 3

```
#### Find max / min number in array:
```python
max(x for x in [0, 10 , 15]) # outputs 15
min(x for x in [0, 10 , 15]) # outputs 0

```

#### How to template string:
```python
# called f strings
x = 'string'
myFString = f'Hi I am an f {x}'
print('myFString', myFstring)
# prints 'Hi I am an f string'
```

#### How to boolean:
```python
x = True
y = False
x == y
# outputs False
```
#### How to Object Literal (in python is Dictionary):
```python
# instantiate empty dict
vowels = {}

# string keys must have quotes else throws error
vowels = { 'a': 0, 'e': 0, 'i':0, 'o': 0, 'u': 0 }
numbers = { 1: a } # this works fine

# must use bracket notation for property lookup
# dot notation will throw an error
vowles['a'] == 0 # True
numbers[1] == 'a' # True
```

#### Property Lookup for Non-existant Key throws error
```python
vowels = { 'a': 0, 'e': 0, 'i':0, 'o': 0, 'u': 0 }
vowels['b'] # throws KeyError: 'b'

# dont use
if vowels[char]: # will thow KeyError if no key
# use
if char in vowels:
```
