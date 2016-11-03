# create a function that takes a list of students, then returns how many candies are own by students under 10

students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

def candies_u10(table):
    result = 0
    for child in table:
        if child['age'] < 10:
            result += child['candies']
        else:
            continue
    return result

print(candies_u10(students))
