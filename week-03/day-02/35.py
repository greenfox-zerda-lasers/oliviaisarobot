# write a function that returns the factorial of a number

def factorial(num):
    result = num
    for x in range(num - 1, 0, -1):
        result *= x
    return result

print(factorial(8))
