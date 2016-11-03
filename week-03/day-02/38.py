# Write a function that returns the minimal element in a list (your own min function)

numbers = [7, 5, 8, -1, 2]

def min(numbers):
    result = numbers[0]
    for x in numbers:
        if x < result:
            result = x
        else:
            continue
    return result

print(min(numbers))
