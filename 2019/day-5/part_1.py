def opcode_compile(opcode):
    """
    The instructions are separated into 2 conditions
    1) One digit instructions
    2) Multiple digit instruction

    Opcode is separated into 2 modes
    1) The ones that have 3 arguments and an operator in between the first two (1 and 2)
    2) The i/o ones (and also the exit one I guess) (3, 4, 99)

    Either one of those can be either in parameter mode or immediate mode
    That's the function of codes_1 and codes_2 respectively
    """
    operations = {1: '+', 2: '*'}
    codes_1 = {0: 'opcode[opcode[i+1]]', 1: 'opcode[i+1]'}
    codes_2 = {0: 'opcode[opcode[i+2]]', 1: 'opcode[i+2]'}

    i = 0
    while i < len(opcode):
        instruct = opcode[i]
        mode_1 = 0
        mode_2 = 0
        if len(str(instruct)) > 2:
            mode_1 = (instruct // 100) % 10
            mode_2 = (instruct // 1000) % 10
            instruct %= 10

        if instruct == 1 or instruct == 2:
            opcode[opcode[i + 3]] = eval(codes_1[mode_1] + operations[instruct] + codes_2[mode_2])
            i += 4
        elif instruct == 3:
            opcode[opcode[i + 1]] = int(input("Digit please: "))
            i += 2
        elif instruct == 4:
            print(opcode[opcode[i + 1]])
            i += 2
        elif instruct == 99:
            return


if __name__ == '__main__':
    with open("input", "r") as file:
        opcode = file.read()

    opcode = [int(n) for n in opcode.split(',')]
    opcode_compile(opcode)
