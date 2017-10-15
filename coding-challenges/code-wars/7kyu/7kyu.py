# PROBLEM 1: Shortest Word
# Given a string of words, return the length of the shortest word(s).
def find_short(sentence):
    # your code here
    sentence = sentence.split()
    shortest = len(sentence[0])
    for word in sentence:
        if len(word) < shortest:
            shortest = len(word)
    print('shortest', shortest)
    return shortest # l: shortest word length

# optimized solution
def find_short(s):
    return min(len(x) for x in s.split())


# PROBLEM 2: Exes and Ohs
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contains any char.
def xo(s):
    s = s.lower()
    print('x count', s.count('x'))
    numX = 0
    numO = 0
    for target in s:
        if target == 'x':
            numX += 1
        elif target == 'o':
            numO += 1
    return numX == numO


# optimized solution
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


# PROBLEM 3: Vowel count
# Return the number (count) of vowels in the given string
def getCount(string):
    vowels = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }
    tally = 0
    for char in string:
        if char in vowels:
            vowels[char] += 1

    for count in vowels:
        tally += vowels[count]

    return tally

# optimized solution v1
def getCount(inputStr):
    x = 0
    for letter in inputStr:
        if letter in 'aeiouAEIOU':
            x += 1
    return x

# optimized solution v2
def getCount(inputStr):
    return sum(1 for letter in inputStr if let in "aeiouAEIOU")
