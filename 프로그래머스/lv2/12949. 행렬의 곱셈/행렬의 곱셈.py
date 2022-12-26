"""
행렬 곱을 위해서는 a행수 = b열수가 같아야 함
"""

def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)): # a의 열
        for j in range(len(arr2[0])): # b의 행
            for k in range(len(arr1[0])): # a의 행(= b의 열)
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    return answer