# Implement union method which combines two arrays.
def linear_search(list, x):
    output = False
    for find in list:
        if find == x:
            output = True
        else:
            continue
    return output

def union(arr1, arr2):
    unique = []
    for x in arr1:
        if linear_search(unique, x) == False:
            unique.append(x)
    for y in arr2:
        if linear_search(unique, y) == False:
            unique.append(y)
        else:
            continue
    return unique

print(union([4,5,6], [1,2,3,4,5,5]))
