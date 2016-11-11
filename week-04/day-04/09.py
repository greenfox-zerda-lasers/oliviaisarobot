# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def separate(word):
    if len(word) <= 0:
        return word
    else:
        return word[0] + "*" + separate(word[1:])





print(separate("greenfox"))
