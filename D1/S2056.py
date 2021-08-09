#2056. 연월일 달력
T = int(input())
month = {
	'01':31, '02':28, '03':31, '04':30, '05':31, '06':30,
    '07':31, '08':31, '09':30, '10':31, '11':30,'12':31
}
for t in range(T):
    case = input()
    mon = case[4:6]
    day = case[6:]
    if mon in month.keys():
        if int(day) <= month[mon]:
            print(f'#{t+1} {case[:4]}/{mon}/{day}')
        else:
            print(f'#{t+1} -1')
    else:
        print(f'#{t+1} -1')