def solution(people, limit):
    answer = 0
    p = sorted(people)
    i, j = 0, len(p)-1
    while i <= j:
        if p[i]+p[j] > limit:
            j -= 1
        else:
            i += 1
            j -= 1
        answer += 1
    return answer

"""
문제풀이 two-pointer
두 리스트 양 끝(제일 작은사람, 큰사람) 비교해서 합보다 크면
맨 뒤사람은 혼자 타야 하는 것이므로 answer++, 맨 끝 포인터 안으로 이동
합이 적으면 같이 타도 되는 것이므로 answer++, 두 포인터 하나씩 안으로 이동
두 포인터가 만나면 리스트 탐색을 끝냄
"""
