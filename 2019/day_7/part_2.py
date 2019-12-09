import itertools


class Amp:
    def __init__(self, opcode, signal, phase):
        self.opcode = opcode
        self.signal = signal
        self.phase = phase

    def opcode_compile(self):
        operations = {1: '+', 2: '*', 7: '<', 8: '=='}
        codes_1 = {0: 'self.opcode[self.opcode[i+1]]', 1: 'self.opcode[i+1]'}
        codes_2 = {0: 'self.opcode[self.opcode[i+2]]', 1: 'self.opcode[i+2]'}
        bools = {True: 1, False: 0}

        i = 0
        while i < len(self.opcode):
            instruct = self.opcode[i]
            mode_1 = 0
            mode_2 = 0
            if len(str(instruct)) > 2:
                mode_1 = (instruct // 100) % 10
                mode_2 = (instruct // 1000) % 10
                instruct %= 10

            if instruct == 1 or instruct == 2:
                self.opcode[self.opcode[i + 3]] = eval(codes_1[mode_1] + operations[instruct] + codes_2[mode_2])
                i += 4
            elif instruct == 3:
                if self.phase >= 0:
                    self.opcode[self.opcode[i + 1]] = self.phase
                    self.phase = -1
                else:
                    self.opcode[self.opcode[i + 1]] = self.signal
                i += 2
            elif instruct == 4:
                yield self.opcode[self.opcode[i + 1]]
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
                self.opcode[self.opcode[i + 3]] = bools[eval(codes_1[mode_1] + operations[instruct] + codes_2[mode_2])]
                i += 4
            elif instruct == 99:
                return -1


if __name__ == '__main__':
    with open("input", "r") as file:
        opcode_str = file.read()

    opcode_int = [int(n) for n in opcode_str.split(',')]
    phase_settings = list(itertools.permutations([9, 8, 7, 6, 5], 5))

    max_value = 0

    for phase in phase_settings:
        amps = []
        amp_methods = []

        # First amp
        amps.append(Amp(opcode_int[:], 0, phase[0]))
        amp_methods.append(amps[0].opcode_compile())
        value = next(amp_methods[0])

        # The rest of the amps
        for j in phase[1:]:
            amps.append(Amp(opcode_int[:], value, j))
            amp_methods.append(amps[-1].opcode_compile())
            value = next(amp_methods[-1])

        # Phases have been inputted, now only values are passed around until
        # code 99 makes one of the generators stop iterating
        i = 0
        while True:
            amps[i].signal = value

            try:
                value = next(amp_methods[i])
            except StopIteration:
                break

            if i == 4:
                i = -1
            i += 1

        # For each permutation check if it yields the largest number
        if value > max_value:
            max_value = value

    print(max_value)
