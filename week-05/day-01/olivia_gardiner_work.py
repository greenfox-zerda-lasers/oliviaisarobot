#def anagramm
#Write a function, that takes two strings and returns a boolean value
#based on if the two strings are Anagramms or not.

#def count_letters
#Write a function, that takes a string as an argument
#and returns a dictionary with all letters in the string as keys,
#and numbers as values that shows how many occurrences there are.

#Now for something completely different
#Send me your work and test file on Slack, and in the afternoon we'll see
#how many of you go through against the tests of others'.

import unicodedata

def anagramm(string1, string2):
    if isinstance(string1, str):
        unicodedata.normalize("NFKD", string1.casefold())
        unicodedata.normalize("NFKD", string2.casefold())
        if string1 != " " and string2 != " ":
            set1 = list(string1)
            set2 = list(string2)
            for letter in set1:
                try:
                    set2.remove(letter)
                except ValueError:
                    return False
            if set2 != []:
                return False
            else:
                return True
        else:
            return False
    else:
        return False

def count_letters(string):
    if any(i.isdigit() for i in string):
        return TypeError
    else:
        frequency = {}
        for letter in string:
            if letter == " ":
                continue
            elif letter.isalpha() or letter.isspace():
                unicodedata.normalize("NFKD", string.casefold())
                frequency[letter] = frequency.get(letter, 0) + 1
        return frequency

#print(anagramm("olivial", "alovii"))
#print(anagramm([2, 1], [1, 2]))
#print(count_letters("olivia gardiner"))
#print(count_letters("olivia 34"))
#print(count_letters("the quick brown fox jumps over the lazy dog"))
