with open("input", "r") as file:
    masses = file.readlines()

print(sum((int(m)//3)-2 for m in masses))
