# Implement linear search method that returns the place of the number in the list, and if the number is not in the list, returns -1. Make it work for multiple matches.
# UNFINISHED!

def linear_search(list, x):
    output = [-1]
    counter = -1
    for find in list:
        counter +=1
        if find == x:
            output = counter
        else:
            continue
    return output

print(linear_search([4, 5, 6, 7, 6], 6))
