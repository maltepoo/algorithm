#1940. 가랏! RC카!
T = int(input())
for tc in range(1, T+1):

    N = int(input()) #command 수
    sp = 0
    dis = 0
    for i in range(N):
        com = list(map(int,input().split()))

        #가속
        if com[0] == 1:
            sp+=com[1]
        #감속
        if com[0] == 2:
            if sp < com[1]: #감속속도>현재속도면 0
                sp = 0
            else:
                sp -= com[1]
        dis += sp
    print('#{} {}'.format(tc, dis))
