a, b, c = map(int, input().split()) #1분 a, 2대 1분b, 3대 1분c
record = [0]*101

for i in range(3):
    r = list(map(int, input().split()))
    for j in range(r[0], r[1]):
        record[j] += 1
print((record.count(1) * a) + (record.count(2) * (2*b)) + (record.count(3) * (3*c)))
#트럭 대수당 요금이기 때문에 2, 3을 각각 곱해줘야 한다