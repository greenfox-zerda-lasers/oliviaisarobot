# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]

def add_number(list):
    if len(list) == 0:
        return 0
    elif type(list[0]) == list:
        return add_number(list[0]) + add_number(list[1:])
    else:
        return list[0] + add_number(list[1:])

print(add_number([1, 2, [3, 4], 1, [1, [2, 4]]]))
