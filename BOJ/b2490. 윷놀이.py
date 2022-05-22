for _ in range(3):
    answer = ['D', 'C', 'B', 'A', 'E']
    yut = sum(map(int, input().split()))
    # 배 0 / 등 1
    print(answer[yut])

    """
    yut = list(map(int, input().split()))
    front, back = 0, 0
    for i in yut:
        if i == 0: front += 1
        else: back += 1
    if front == 1:
        print("A")
    elif front == 2:
        print("B")
    elif front == 3:
        print("C")
    elif front == 4:
        print("D")
    elif back == 4:
        print("E")
    """