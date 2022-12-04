def part1(today):
    mmax = 0
    cur = 0
    for i in today:
        if i == "" or i == "\n":
            if cur > mmax:
                mmax = cur
                cur = 0
        else:
            cur += int(i)
    return max(cur, mmax)



def part2(today):
    mmax = [0,0,0]
    cur = 0
    for i in today:
        if i == "" or i == "\n":
            if cur > mmax[2]:
                mmax[2] = cur
                mmax.sort(reverse=True)
            cur = 0
            continue
        cur += int(i)

    return sum(mmax)


with open("/Users/nic/Documents/aoc22/aoc2022/day1_input.txt") as f:
    today = f.read().split('\n')

print(part1(today))
print(part2(today))
