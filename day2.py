def calcday(day):
    ret = 0
    n1,n2 = day.split()
    #print(n1,n2)
    # x,y,z = 1,2,3
    # lose, draw, win = 0, 3, 6
    throw = {'X': 1, 'Y': 2, 'Z': 3}
    result = {'win': 6, 'lose': 0, 'draw': 3}

    if n1 == 'A':
        if n2 == 'X':
            ret = throw[n2] + result['draw']
        elif n2 == 'Y':
            ret = throw[n2] + result['win']
        elif n2 == 'Z':
            ret = throw[n2] + result['lose']
    elif n1 == 'B':
        if n2 == 'X':
            ret = throw[n2] + result['lose']
        elif n2 == 'Y':
            ret = throw[n2] + result['draw']
        elif n2 == 'Z':
            ret = throw[n2] + result['win']
    elif n1 == 'C':
        if n2 == 'X':
            ret = throw[n2] + result['win']
        elif n2 == 'Y':
            ret = throw[n2] + result['lose']
        elif n2 == 'Z':
            ret = throw[n2] + result['draw']
    #print(ret)
    return ret

def calcday2(day):
    #A rock, B paper, C scissors
    #X Lose, Y Draw, Z Win
    # x,y,z = 1,2,3
    # lose, draw, win = 0, 3, 6
    ret = 0
    n1,n2 = day.split()
    r = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    result = {'win': 6, 'lose': 0, 'draw': 3}
    throw = {'rock': 1, 'paper': 2, 'scissors': 3}

    if n2 == "X":
        if n1 == 'A':
            ret = result[r[n2]] + throw['scissors']
        elif n1 == 'B':
            ret = result[r[n2]] + throw['rock']
        elif n1 == 'C':
            ret = result[r[n2]] + throw['paper']
    elif n2 == "Y":
        if n1 == 'A':
            ret = result[r[n2]] + throw['rock']
        elif n1 == 'B':
            ret = result[r[n2]] + throw['paper']
        elif n1 == 'C':
            ret = result[r[n2]] + throw['scissors']
    elif n2 == "Z":
        if n1 == 'A':
            ret = result[r[n2]] + throw['paper']
        elif n1 == 'B':
            ret = result[r[n2]] + throw['scissors']
        elif n1 == 'C':
            ret = result[r[n2]] + throw['rock']
    return ret



with open("/Users/nic/Documents/aoc22/day2_input.txt") as f:
    today = f.read().split('\n')[:-1]
#A rock, B paper, C scissors
#X Rock, Y Paper, Z Scissors
summer = 0
for i in today:
    summer += calcday2(i)
print(summer)
