lower_limit = 130254
upper_limit = 678275

# There are 2 filters to this task
# Filter #1 | The numbers have to be sorted from smallest to highest so I check for that
# Filter #2 | The numbers have to have at least one adjacent repeating digit and since they're
# sorted those digits are always next to each other so I just check if there are any repeating digits
# and if so the number passes the filter
pw_amount = 0
for i in range(lower_limit, upper_limit):
    i = [int(n) for n in list(str(i))]
    if i == sorted(i) and (len(set(i)) < len(i)):
        pw_amount += 1

print(pw_amount)
