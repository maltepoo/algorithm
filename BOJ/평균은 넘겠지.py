c = int(input())
for i in range(c):
    scores = list(map(int, input().split()))
    sc = scores[0]
    avg = sum(scores[1:])/sc
    stu = 0
    for s in scores[1:]:
        if s > avg:
            stu += 1
    print("{:0.3f}%".format(stu/sc*100))