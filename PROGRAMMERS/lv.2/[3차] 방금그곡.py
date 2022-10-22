def change_melody(m):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return m

def generate_music(melody, time):
    if len(melody) < time:
        melody = melody * (time // len(melody) + 1)
    return melody[:time]

def solution(m, musicinfos):
    answer = ''
    res = []
    m = change_melody(m)
    for i in range(len(musicinfos)):
        musicinfo = musicinfos[i]
        st, ed, title, score = musicinfo.split(",")
        score = change_melody(score)
        playtime = (int(ed[0:2]) - int(st[0:2])) * 60 + (int(ed[3:]) - int(st[3:]))

        played = generate_music(score, playtime)
        if m in played:
            res.append((i, title, playtime))

    if res:
        res.sort(key=lambda x: x[2], reverse=True)  # 재생시간 우선순위 정렬
        answer = res[0]  # 최대 재생시간
        for i in range(len(res)):
            if res[i][2] >= answer[2] and res[i][0] < answer[0]:
                answer = res[i]
        return answer[1]
    else:
        return "(None)"

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABCDEFG", ["11:50,12:04,HELLO,CDEFGAB", "12:57,13:11,BYE,CDEFGAB"]))