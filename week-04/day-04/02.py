# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def add_up_to(n):
    if n == 0:
        return 0
    else:
        return n + add_up_to(n-1)

print(add_up_to(9))
