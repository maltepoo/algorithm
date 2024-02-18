import sys
sys.setrecursionlimit(10**6)


def postorder(arr):
    if len(arr) == 0:
        return

    mid = len(arr) # 오른쪽 노드가 없을 경우 무한루프에 빠지지 않도록 함
    # r을 기준으로 왼/오 트리를 나누어준다
    for i in range(1, len(arr)):
        if arr[0] < arr[i]:
            mid = i
            break

    postorder(arr[1:mid])
    postorder(arr[mid:])
    print(arr[0])


nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break

postorder(nodes)