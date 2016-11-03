# write a function that filters the odd numbers from a list and returns a new list consisting only the evens

numbers = [3, 4, 5, 6, 7]

def only_even(numbers):
    result = []
    for x in numbers:
        if x%2 is 0:
            result.append(x)
        else:
            continue
    return result

print(only_even(numbers))
