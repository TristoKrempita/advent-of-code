def calc_zeroth_value(opcode):
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
