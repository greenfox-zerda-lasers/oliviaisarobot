ab = 123

credits = 100

is_bonus = False

if credits > 50 and is_bonus is False:
    print(ab - 2)
elif credits < 50 and is_bonus is False:
    print(ab - 1)
elif is_bonus is True:
    print(ab)
