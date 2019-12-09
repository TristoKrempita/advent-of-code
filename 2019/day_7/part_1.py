import itertools


def opcode_compile(opcode, signal, phase=-1):
    operations = {1: '+', 2: '*', 7: '<', 8: '=='}
    codes_1 = {0: 'opcode[opcode[i+1]]', 1: 'opcode[i+1]'}
    codes_2 = {0: 'opcode[opcode[i+2]]', 1: 'opcode[i+2]'}
    bools = {True: 1, False: 0}

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
            if phase >= 0:
                opcode[opcode[i + 1]] = phase
                phase = -1
            else:
                opcode[opcode[i + 1]] = signal
            i += 2
        elif instruct == 4:
            yield opcode[opcode[i + 1]]
            i += 2
        elif instruct == 5:
            if eval(codes_1[mode_1]):
                i = eval(codes_2[mode_2])
            else:
                i += 3
        elif instruct == 6:
            if not eval(codes_1[mode_1]):
                i = eval(codes_2[mode_2])
            else:
                i += 3
        elif instruct == 7 or instruct == 8:
            opcode[opcode[i + 3]] = bools[eval(codes_1[mode_1] + operations[instruct] + codes_2[mode_2])]
            i += 4
        elif instruct == 99:
            return


if __name__ == '__main__':
    with open("input", "r") as file:
        opcode = file.read()

    opcode = [int(n) for n in opcode.split(',')]
    max_value = 0
    phase_settings = list(itertools.permutations([0, 1, 2, 3, 4], 5))

    for phase in phase_settings:
        value = next(opcode_compile(opcode, 0, phase[0]))

        for j in phase[1:]:
            value = next(opcode_compile(opcode, value, j))

        if value > max_value:
            max_value = value

    print(max_value)
