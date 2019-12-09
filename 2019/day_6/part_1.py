def get_path_length(pairs, planet):
    path_length = 0
    while True:
        if pairs.get(planet):
            planet = pairs[planet]
            path_length += 1
        else:
            return path_length


if __name__ == '__main__':
    with open("input", "r") as file:
        orbits = file.read().splitlines()

    planet_pairs = dict()

    for planet_tuple in [(n.split(')')[1], n.split(')')[0]) for n in orbits]:
        planet_pairs[planet_tuple[0]] = planet_tuple[1]

    print(sum((get_path_length(planet_pairs, key)) for key in planet_pairs))
