def convertToMin(str_min):
    str_min = str_min.split(":")
    return (int(str_min[0])*60) + int(str_min[1])

def solution(book_time):
    rooms = [0 for _ in range(24*60 + 10)]

    for b in book_time:
        roomIn, roomOut = convertToMin(b[0]), convertToMin(b[1]) + 10
        
        rooms[roomIn] += 1
        rooms[roomOut] -= 1
    
    # 누적합으로 가장 방이 많이 필요했던 시간은 언제인지 찾으면 답이된다
    for i in range(1, len(rooms)):
        rooms[i] = rooms[i-1] + rooms[i]
        
    return max(rooms)