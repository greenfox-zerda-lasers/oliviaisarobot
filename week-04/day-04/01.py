# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def count_down(n):
    if n <= 1:
        print(1)
        return 1
    else:
        print(n)
        return count_down(n-1)

count_down(6)
