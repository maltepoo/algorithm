n, m = map(int, input().split())
hear = [input() for _ in range(n)]
see = [input() for _ in range(m)]
total = list(set(hear) & set(see))
print(len(total), *sorted(total), sep="\n")