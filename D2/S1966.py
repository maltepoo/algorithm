#1966. 숫자를 정렬하자

def bubbleSort(a):
    #기준값과 바로 옆 값 비교해나가며 정렬하는 방법, 범위는 끝에서 -1
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return arr

def countingSort(a, r, cnt):
    #원소끼리 비교를 하지 않고 원소가 몇번 등장하는지 갯수를 세서 정렬하는 방법
    #a는 정렬할 배열, r는 정렬된 값 저장할 빈 배열, cnt는 카운트를 넣을 배열
    for i in a:
        cnt[i] += 1
    for i in range(len(cnt)-1):
        cnt[i+1] += cnt[i]
    for i in range(len(a)-1, -1, -1):
        r[cnt[a[i]]-1] = a[i]
        cnt[a[i]] -= 1
    return r


def selectionSort(a):
    #제일 작은 값을 구하고 그 값을 맨 처음으로 이동시켜 정렬하는 방법, 범위는 앞에서 +1
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_c = [-1 for _ in range(len(arr))]
    cnt = [0 for _ in range(max(arr)+1)]

    print('#{} '.format(tc))
    print(*selectionSort(arr))
    print(*bubbleSort(arr))
    print(*countingSort(arr, arr_c, cnt))