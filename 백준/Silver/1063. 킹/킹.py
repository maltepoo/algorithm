k, s, n = input().split(" ")
direction = [input() for _ in range(int(n))]

dir = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (-1, 0),
    'T': (1, 0),
    'RT': (1, 1),
    'LT': (1, -1),
    'RB': (-1, 1),
    'LB': (-1, -1)
}

kx, ky = (ord(k[0]) - 65), int(k[1]) - 1
sx, sy = (ord(s[0]) - 65), int(s[1]) - 1

for d in direction:
    nky, nkx = ky + dir[d][0], kx + dir[d][1]
    nsy, nsx = sy + dir[d][0], sx + dir[d][1]

    if 0 <= nky < 8 and 0 <= nkx < 8: #킹의 새 위치가 범위내에 있고
        if nky == sy and nkx == sx: #새킹, 돌의 위치가 겹치면
            if 0 <= nsy < 8 and 0 <= nsx < 8: #옮긴 돌이 범위 내이면 두 돌 옮김
                ky, kx = nky, nkx
                sy, sx = nsy, nsx
        else: #킹의 새 위치가 돌괴 겹치지 않을때
            ky, kx = nky, nkx
    else: continue
print(chr(kx + 65)+str(ky + 1))
print(chr(sx + 65)+str(sy + 1))