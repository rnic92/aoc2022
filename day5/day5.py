import sys

with open("/Users/nic/Documents/aoc22/aoc2022/day5/day5_input.txt") as f:
    today = f.read().split('\n')[:-1]

starting, directions = today[:8], today[10:]

# converts "move 2 from 9 to 7"  ---> [2, 9, 7]
dir2 = [x.split(' ') for x in directions]
dir2 = [[int(x[1]),int(x[3]),int(x[5])] for x in dir2]

def part1():
    # creates dictionary as [1: , 2: , 3: , 4: , 5: ....] as the starting stack
    stacks = {key:[] for key in range(1, len(starting)+2)}
    for row in starting:
        if row[1] != ' ':
            stacks[1].append(row[1])
        if row[5] != ' ':
            stacks[2].append(row[5])
        if row[9] != ' ':
            stacks[3].append(row[9])
        if row[13] != ' ':
            stacks[4].append(row[13])
        if row[17] != ' ':
            stacks[5].append(row[17])
        if row[21] != ' ':
            stacks[6].append(row[21])
        if row[25] != ' ':
            stacks[7].append(row[25])
        if row[29] != ' ':
            stacks[8].append(row[29])
        if row[33] != ' ':
            stacks[9].append(row[33])

    # reverse them to be upright
    for i in stacks.keys():
        stacks[i].reverse()

    for i in dir2:
        moves = i[0]
        origination = i[1]
        endstack = i[2]
        for j in range(moves):
            n = stacks[origination].pop()
            stacks[endstack].append(n)


    for i in stacks.keys():
        print(stacks[i][-1], end='')
    print()


def part2():
    stacks = {key:[] for key in range(1, len(starting)+2)}
    for row in starting:
        if row[1] != ' ':
            stacks[1].append(row[1])
        if row[5] != ' ':
            stacks[2].append(row[5])
        if row[9] != ' ':
            stacks[3].append(row[9])
        if row[13] != ' ':
            stacks[4].append(row[13])
        if row[17] != ' ':
            stacks[5].append(row[17])
        if row[21] != ' ':
            stacks[6].append(row[21])
        if row[25] != ' ':
            stacks[7].append(row[25])
        if row[29] != ' ':
            stacks[8].append(row[29])
        if row[33] != ' ':
            stacks[9].append(row[33])
    for i in stacks.keys():
        stacks[i].reverse()
    for i in dir2:
        boxes_moved = i[0]
        origination = i[1]
        endstack = i[2]
        n = stacks[origination][-boxes_moved:]
        stacks[origination] = stacks[origination][:-boxes_moved]
        stacks[endstack] = stacks[endstack] + n

    for i in stacks.keys():
        print(stacks[i][-1], end='')
    print()

if len(sys.argv) < 2:
    part_to_run = input("enter which part to run: ")
else:
    part_to_run = sys.argv[1]
if  part_to_run == "1":
    part1()
else:
    part2()
