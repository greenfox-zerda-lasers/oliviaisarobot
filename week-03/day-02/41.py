# create a function that counts the students that has more than 4 candies

students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

def more_than_four(table):
    result = 0
    for child in table:
        if child['candies'] > 4:
            result += 1
        else:
            continue
    return result

print(more_than_four(students))
