# Implement bubble sort method.
# If remaining pairs are sorted, stop running the fuction.

numbers = [3,9,4,5,2,1]

new = [1,2,3,4,5,6]

def issorted(list):
    for x in list:
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                output = False
                break
            else:
                output = True
    return output

print(issorted(new))

def bubble_sort(list):
    if issorted(list) == False:
        for x in list:
            for i in range(len(list)-1):
                if list[i] > list[i+1]:
                    temp = list[i]
                    list[i] = list[i+1]
                    list[i+1] = temp
    elif issorted(list) == True:
        return list
    return list

print(bubble_sort(numbers))
