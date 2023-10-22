t = int(input())


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


def recursion(s, left, right):
    global cnt
    if left >= right:
        return 1
    elif s[left] != s[right]:
        return 0
    else:
        cnt += 1
        return recursion(s, left+1, right-1)

for _ in range(t):
    cnt = 1
    print(isPalindrome(input()), cnt)