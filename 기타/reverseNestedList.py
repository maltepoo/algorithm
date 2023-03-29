"""
배열이 몇 번 중첩되었는지 나타내는 n과
배열 li이 주어진다.
"""
n = 4
li = [1, 2, 3, [4, 5, [6, [7]]]]

#풀이1
def rev(l):
    l.reverse()
    print(li)
    for i in l:
        if type(i) == list:
            rev(i)
rev(li)
