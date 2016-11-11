# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def power_to(n, x):
    if x <= 0:
        return 1
    else:
        x = x-1
        return n*power_to(n, x)

print(power_to(2, 10))
