def is_palindrome(text):
    """
    >>> is_palindrome('Mr. Owl ate my metal worm')
    True
    >>> is_palindrome('Eva, can I see bees in a cave?')
    True
    """
    words_can = []
    for letter in text:
        if letter.isalpha():
            words_can.append(letter)
        
    return ''.join(words_can).lower() == ''.join(words_can).lower()[::-1]

def is_isogram(text):
    """
    >>> is_isogram('uncopyrightables')
    True
    """
    return len(text) == len(set(text))

def is_pangram(text):
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    words_can = []
    
    for letter in text:
        if letter.isalpha():
            words_can.append(letter)
    
    for letter in range(len(alphabet)):
        if alphabet[0] in words_can:
            alphabet.pop(0)
    
    return alphabet == []

def is_anagram(text1, text2):
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    words_can_1 = []
    words_can_2 = []
    
    for letter in text1:
        if letter.isalpha():
            words_can_1.append(letter.lower())
    
    for letter in text2:
        if letter.isalpha():
            words_can_2.append(letter.lower())
            
    return words_can_1.sort() == words_can_2.sort()
            
def is_blanagram(text1, text2):
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
    words_can_1 = []
    words_can_2 = []
    
    for letter in text1:
        if letter.isalpha():
            words_can_1.append(letter.lower())
    
    for letter in text2:
        if letter.isalpha():
            words_can_2.append(letter.lower())

    if len(words_can_1) == len(words_can_2):
        for letter in words_can_1:
            if letter in  words_can_2:
                words_can_2.remove(letter)
        print(len(words_can_2))
        return len(words_can_2) == 1
