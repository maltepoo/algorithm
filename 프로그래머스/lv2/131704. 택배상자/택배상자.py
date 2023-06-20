def solution(order):
    belt = []

    n, i = 1, 0
    while n < len(order) + 1:
        belt.append(n)
        while belt[-1] == order[i]:
            belt.pop()
            i += 1

            if len(belt) == 0:
                break
        n += 1
    return i