def calc_zeroth_value(opcode):
    """ Steps through the opcode 4 numbers at a time, first for command type, second and third for address of values
     and fourth for address to store result in"""
    for i in range(0, len(opcode), 4):
        if opcode[i] == 1:
            opcode[opcode[i + 3]] = opcode[opcode[i + 1]] + opcode[opcode[i + 2]]
        elif opcode[i] == 2:
            opcode[opcode[i + 3]] = opcode[opcode[i + 1]] * opcode[opcode[i + 2]]
        elif opcode[i] == 99:
            return opcode


if __name__ == '__main__':
    with open("input", "r") as file:
        opcode = file.read()

    opcode = [int(n) for n in opcode.split(',')]

    print(calc_zeroth_value(opcode))
