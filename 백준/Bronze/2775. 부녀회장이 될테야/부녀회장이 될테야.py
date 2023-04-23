building = [[j+1 for j in range(15)] for i in range(15)]
for i in range(1, 15):
    for j in range(15):
        # a층의 b호에 사려면 아래층의 1호부터 b호 까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
        building[i][j] = sum(building[i-1][:j+1])

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(building[k][n-1])