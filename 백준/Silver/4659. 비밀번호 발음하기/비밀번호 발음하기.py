moeum = 'aeiou'
excpt = ('ee', 'oo')


def check_case1(now):
    if now in moeum:
        return True
    return False


def make_mz(now):
    if now in moeum:
        return 'm'
    return 'z'


def check_case3(s1, s2):
    if s1 != s2:
        return True
    elif s1+s2 in excpt:
        return True
    return False


while True:
    t = input().rstrip()
    if t == 'end':
        break

    case1 = False
    case2_word = ""
    case2 = True
    case3_word = ""
    case3 = True
    for i in range(len(t)):
        if not case1 and check_case1(t[i]): #case1
            case1 = True

        case2_word += make_mz(t[i]) #case2
        lst_three = case2_word[-3:]
        if lst_three == 'mmm' or lst_three == 'zzz':
            case2 = False

        case3_word += t[i] #case3
        if len(case3_word) >= 2 and not check_case3(case3_word[-1], case3_word[-2]):
            case3 = False

    if case1 and case2 and case3:
        print('<{}> is acceptable.'.format(t))
    else: print('<{}> is not acceptable.'.format(t))