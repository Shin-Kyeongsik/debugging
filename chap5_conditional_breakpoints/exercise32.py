multiples_of_twelve = []
other_nums = []
for i in range(1000):
    if i % 12 == 0: # BP: i % 12 == 0
        multiples_of_twelve.append(i)
    else:
        other_nums.append(i)