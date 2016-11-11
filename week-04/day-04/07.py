# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def change(word):
    if len(word) <= 0:
        return word
    else:
        if word[0] == "x":
            return "y" + change(word[1:])
        else:
            return word[0] + change(word[1:])

print(change("green fox"))
