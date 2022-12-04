def overlapers(day):
    elf1, elf2 = day.split(',')
    elf1 = [int(x) for x in elf1.split('-')]
    elf2 = [int(x) for x in elf2.split('-')]

    if elf1[0] <= elf2[0] and elf1[1] >= elf2[0]:
        # 2-4, 3-5
        return 1
    elif elf2[0] <= elf1[0] and elf2[1] >= elf1[0]:
        # 3-5, 2-4
        return 1
    else:
        return 0


with open("/Users/nic/Documents/aoc22/day4_input.txt") as f:
    today4 = f.read().split('\n')[:-1]

total = 0
for day in today4:
    total += overlapers(day)
print(total)
