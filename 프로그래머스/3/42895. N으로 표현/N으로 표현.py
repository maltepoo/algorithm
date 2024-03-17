def solution(N, number):
    result = []

    for n in range(1, 9):
        part = set()
        part.add(int(str(N)*n))

        for i in range(n-1):
            for op1 in result[i]:
                for op2 in result[-i-1]:
                    part.add(op1 + op2)
                    part.add(op1 * op2)
                    part.add(op1 - op2)
                    if op2 != 0:
                        part.add(op1 / op2)
        if number in part:
            return n
        result.append(part)
    return -1