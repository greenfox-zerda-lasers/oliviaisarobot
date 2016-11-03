# Implement binary search, wich tests if the param is sorted, sorts if not and search for the other param.

numbers = [3,9,4,5,2,1]

def issorted(list):
    for x in list:
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                output = False
                break
            else:
                output = True
    return output

def bubble_sort(list):
    for x in list:
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list

def binary_search(list, num):
    if issorted(list) == False:
        list = bubble_sort(list)
    output = False
    first = 0
    last = len(list)-1
    while first <= last and output is False:
        halfpoint = (first + last)//2
        if num == list[halfpoint]:
            output = True
        else:
            if num < list[halfpoint]:
                last = halfpoint-1
            else:
                first = halfpoint+1
    return output

print(binary_search([4,5,6], 6))
