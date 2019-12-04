from part_1 import draw

with open("input", "r") as file:
    lines = file.read()

lines = lines.split('\n')
first_line = lines[0].split(',')
second_line = lines[1].split(',')

arr1 = []
arr2 = []
for i in draw(first_line):
    arr1.append(i)
for j in draw(second_line):
    arr2.append(j)


def len_to_intersection(coord, line):
    """ Steps through every dot that makes a line until the line reaches the desired coordinate
    and returns the Manhattan length"""
    line_len = 0
    for dot in draw(line):
        if dot == coord:
            return line_len
        else:
            line_len += 1


a = []
# list(set(arr1) & set(arr2)) finds which dots overlap in both lines
for coord in list(set(arr1) & set(arr2)):
    len_first = len_to_intersection(coord, first_line)
    len_second = len_to_intersection(coord, second_line)
    a.append(len_first+len_second)

print(sorted(a)[1])
