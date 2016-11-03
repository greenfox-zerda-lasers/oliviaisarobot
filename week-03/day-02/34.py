# write a function that returns the sum of the list

numbers = [4, 5, 6, 7, 8, 9, 10]

def sum(numbers):
    result = 0
    for x in numbers:
        result = result + x
    return result

print(sum(numbers))
