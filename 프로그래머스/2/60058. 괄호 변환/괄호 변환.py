def divide(s):
    left, right = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            return s[:i + 1], s[i + 1:]
    return s, ''


def is_correct_str(st):
    arr = []
    for s in st:
        if s == '(':
            arr.append(s)
        else:
            if not arr:
                return False
            else:
                arr.pop()
    return True


def braket_convert(s):
    result = ''
    if s == '':
        return ''

    u, v = divide(s)
    if is_correct_str(u):
        result = u + braket_convert(v)
    else:
        result = '(' + braket_convert(v) + ')'
        for temp in u[1:-1]:
            if temp == '(':
                result += ')'
            else:
                result += '('

    return result


def solution(p):
    if p == '':
        return ''
    return braket_convert(p)