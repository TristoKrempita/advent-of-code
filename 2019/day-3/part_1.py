with open("input", "r") as file:
    lines = file.read()

lines = lines.split('\n')
first_line = lines[0].split(',')
second_line = lines[1].split(',')


def draw(line):
    """ Gets the x and y coordinate of every dot that makes this line"""
    red, stup = 0, 0
    for item in line:
        if item[0] == "L":
            for i in range(int(item[1:])):
                yield red, stup-i
            stup = stup-int(item[1:])
        elif item[0] == "R":
            for i in range(int(item[1:])):
                yield red, stup+i
            stup = stup+int(item[1:])
        elif item[0] == "U":
            for i in range(int(item[1:])):
                yield red+i, stup
            red = red+int(item[1:])
        elif item[0] == "D":
            for i in range(int(item[1:])):
                yield red - i, stup
            red = red-int(item[1:])


arr1 = []
arr2 = []
for i in draw(first_line):
    arr1.append(i)
for j in draw(second_line):
    arr2.append(j)


if __name__ == '__main__':
    # list(set(arr1) & set(arr2)) finds which dots overlap in both lines
    print(sorted([abs(i[0])+abs(i[1]) for i in list(set(arr1) & set(arr2))])[1])
