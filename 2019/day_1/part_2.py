with open("input", "r") as file:
    masses = file.readlines()


def calc_fuel(mass):
    if mass//3-2 < 0:
        return mass
    else:
        return mass + calc_fuel(mass//3-2)


print(sum(calc_fuel(int(m))-int(m) for m in masses))
