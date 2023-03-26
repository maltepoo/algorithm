def solution(genres, plays):
    answer = []
    
    total_plays = {}
    for g, p in zip(genres, plays):
        if g in total_plays:
            total_plays[g] += p
        else: total_plays[g] = p
    
    genre_rank = list(dict(sorted(total_plays.items(), key = lambda x: x[1], reverse=True)).keys())
    songs = sorted(zip(genres, plays, [i for i in range(len(plays))]), key=lambda x:(-x[1], x[2]))
    print(genre_rank)
    print(songs)
    
    for gen in genre_rank:
        for s in songs:
            name, plays, idx = s
            if gen == name:
                songs.remove(s)
                answer.append(idx)
                break
        for s in songs:
            name, plays, idx = s
            if gen == name:
                songs.remove(s)
                answer.append(idx)
                break
    return answer