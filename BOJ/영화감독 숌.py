endNums = [666]
def newEndNum(num):
    i = 1666
    while True:
        if len(endNums) >= num:
            return endNums[num-1]
        elif "666" in str(i):
            endNums.append(i)
        i += 1
print(newEndNum(int(input())))