# create a function that returns the shortest string from a list

names = ['Zakarias', 'Hans', 'Otto', 'Ole']

def shortest(names):
    sh = len(names[0])
    for x in names:
        if len(x) < sh:
            sh = len(x)
        else:
            continue
    for y in names:
        if len(y) == sh:
            result = y
        else:
            continue
    return result


print(shortest(names))
