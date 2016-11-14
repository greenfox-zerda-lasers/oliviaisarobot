# Adds a and b, returns as result
def add(a, b):
    if a + b == 5:
        return 5

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    list = sorted(pool)
    if len(pool)%2 == 0:
        return list[int(len(pool)/2)]
    else:
        return (list[int(len(pool)/2)] + (list[int(len(pool)/2)]-1)) / 2

# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aáeéiíoóöőuúüű'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    if teve != teve.isalpha():
        return TypeError
    else:
        for char in teve:
            if is_vovel(char):
                teve = (char+'v'+char).join(teve.split(char))
        return teve
