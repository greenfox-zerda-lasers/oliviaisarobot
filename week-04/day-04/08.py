# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def delete(word):
    if len(word) <= 0:
        return word
    else:
        if word[0] == "x":
            return "" + delete(word[1:])
        else:
            return word[0] + delete(word[1:])

print(delete("green fox"))
