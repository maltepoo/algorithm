import math

def solution(fees, records):
    answer = []
    inoutRecord = {}
    parking = {}
    basicTime, basicFee, unitTime, unitFee = map(int, fees)
    
    for rc in records:
        time, carNum, status = rc.split(" ")
        h, m = time.split(":")
        time = int(h)*60 + int(m)
        
        if status == 'IN':
            inoutRecord[carNum] = time
        elif status == 'OUT':
            fee = 0
            parkingTime = time - inoutRecord[carNum]
            del inoutRecord[carNum]
            
            if carNum in parking:
                parking[carNum] += parkingTime
            else: parking[carNum] = parkingTime
    
    # 23:59분 출차로 계산할 데이터들
    # 1439분 (23:59)
    for c, t in inoutRecord.items():
        time = 1439-t
        if c in parking:
                parking[c] += time
        else: parking[c] = time
    
    for c, t in sorted(parking.items()):
        if t >= basicTime:
            answer.append(basicFee+(math.ceil((t-basicTime)/unitTime))*unitFee)
        else: answer.append(basicFee)
    
    return answer