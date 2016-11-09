from collections import Counter
from prettytable import PrettyTable

# Create a method that returns the five most frequent lottery number in a pretty table format
def five_most_frequent(file_name):
    f = open(file_name)
    text = f.readlines()
    numbers = []
    for line in text:
        array = line.split(";")
        for number in array[-5:]:
            numbers.append(int(number))

    st = Counter(numbers).most_common(5)

    first = st[0]
    first_num = first[0]
    first_freq = first[1]
    second = st[1]
    second_num = second[0]
    second_freq = second[1]
    third = st[2]
    third_num = third[0]
    third_freq = third[1]
    fourth = st[3]
    fourth_num = fourth[0]
    fourth_freq = fourth[1]
    fifth = st[4]
    fifth_num = fifth[0]
    fifth_freq = fifth[1]

    table = PrettyTable(["number", "frequency"])
    table.add_row([first_num, first_freq])
    table.add_row([second_num, second_freq])
    table.add_row([third_num, third_freq])
    table.add_row([fourth_num, fourth_freq])
    table.add_row([fifth_num, fifth_freq])

    table.sortby = "frequency"
    table.reversesort = True

    return table.get_string()

print(five_most_frequent("otos.csv"))
