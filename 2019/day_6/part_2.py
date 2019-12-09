def get_path(pairs, planet):
    path = []
    while True:
        if pairs.get(planet):
            path.append(planet)
            planet = pairs[planet]
        else:
            return path


def get_shortest_path(me, santa):
    length = 0
    for element in me:
        length += 1
        if element in santa:
            for _ in santa[:santa.index(element)][::-1]:
                length += 1
            return length - 3


if __name__ == '__main__':
    with open("input", "r") as file:
        orbits = file.read().splitlines()

    planet_pairs = dict()

    for planet_tuple in [(n.split(')')[1], n.split(')')[0]) for n in orbits]:
        planet_pairs[planet_tuple[0]] = planet_tuple[1]

    my_path = (get_path(planet_pairs, 'YOU'))
    santas_path = (get_path(planet_pairs, 'SAN'))

    print(get_shortest_path(my_path, santas_path))
