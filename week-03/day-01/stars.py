de = 0

for x in range(11):
    if x < 6:
        print("* " * x)
    elif x is 5:
        continue
    else:
        de += 2
        print("* " * (x - de))
