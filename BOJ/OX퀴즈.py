t = int(input())
for i in range(t):
    tc = input()
    score, conti = 0, 0
    for j in tc:
        if j == 'X':
            conti = 0
        else:
            conti += 1
        score += conti
    print(score)