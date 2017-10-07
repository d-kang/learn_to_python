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
# works for any iterable: string, array, dictionary
# works like forEach method
# iterates over elems not over index
for x in list:

# when iterating over dictionary, it iterates over keys
```
#### How to for loop over range of numbers:
```python
# to iterate
for x in range(0, 5):
    print(x)
# 0
# 1
# 2
# 3
# 4

# to skip over add third arg to range
for x in range(0, 5, 2):
    print(x)
# 0
# 2
# 4
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

# string.split('') will throw an error
```

#### How to split string into array of characters?
```python
string = 'the brown cow'
arrToStr = list(string)
# ['t', 'h', 'e', ' ', 'b', 'r', 'o', 'w', 'n', ' ', 'c', 'o', 'w']
```

#### How to instantiate empty var:
```python
value = None
```

#### How to increment:
```python
num += 1
# num++ is invalid
```

#### How to lower case:
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

#### How to add up nums in array
```python
sum([1, 2, 3, 4])
# 10

sum(1 for x in 'hello')
# 5

sum(2 for x in 'hello')
# 10

sum(1 for x in 'hello' if x == 'l')
# 2
```
