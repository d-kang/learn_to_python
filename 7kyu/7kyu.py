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
