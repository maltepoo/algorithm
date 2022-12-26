"""
최소공배수는 두 자연수의 곱 / 최대 공약수
"""

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def solution(arr):
    while len(arr) > 1:
        a, b = arr.pop(), arr.pop()
        arr.append((a*b)//gcd(a, b))
    return arr[0]