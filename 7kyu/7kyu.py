# shortest word
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


# Exes and Ohs
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

s = 'xkoGJxCoxooxxoooSoLoxxbmAQoxxNdoxfxxrxEhpoooxooxoxx'
print('xo(s)', xo(s))
