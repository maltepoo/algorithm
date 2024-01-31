def solution(bandage, health, attacks):
    bt, r, ad = bandage
    hp = health

    time = attacks[0][0]
    hp -= attacks[0][1]
    for atk, dmg in attacks[1:]:
        t = atk - time - 1
        if t // bt > 0:
            hp += ((t // bt) * ad) + ((bt * r) * (t // bt))
        hp += r * (t % bt)
        
        if 1 > hp - dmg:
            return -1

        if hp > health:
            hp = health

        time = atk
        hp -= dmg
    return hp