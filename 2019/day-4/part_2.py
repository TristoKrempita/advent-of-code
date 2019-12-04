lower_limit = 130254
upper_limit = 678275

# This one has the same logic except I check that if there are numbers repeating more than twice
# there are also some numbers repeating exactly twice
pw_amount = 0
for i in range(lower_limit, upper_limit):
    i = [int(n) for n in list(str(i))]
    rep = [i.count(n) for n in set(i)]
    if i == sorted(i) and (len(set(i)) < len(i)) and all(n >= 1 for n in rep):
        if 2 in rep:
            pw_amount += 1

print(pw_amount)
