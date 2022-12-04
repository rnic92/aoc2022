def calcday3(pack):
    p1,p2 = pack[:len(pack)//2], pack[len(pack)//2:]
    dif = set(p1).intersection(set(p2))

    return values[next(iter(dif))]

def calcday32(packs):
    #print(packs)
    ret = set(packs[0]).intersection(set(packs[1])).intersection(set(packs[2]))
    return values[next(iter(ret))]




with open("/Users/nic/Documents/aoc22/day3_input.txt") as f:
    today = f.read().split('\n')[:-1]
values = {char:idx for idx, char in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 1)}


sumone = 0
for i in today:
    sumone += calcday3(i)
print(sumone)



n = 0
team = []
total = 0
for i in today:
    team.append(i)
    n+=1
    if n == 3:
        total += calcday32(team)
        team = []
        n = 0

print(total)
