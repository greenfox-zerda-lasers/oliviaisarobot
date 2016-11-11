# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

output = 0

def sum(n):
    global output
    if n <= 0:
        return 0
    elif n >= 10:
        output += n%10
        return sum(n//10)
    else:
        output += n
        return output

print(sum(569))
