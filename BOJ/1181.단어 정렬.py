n = int(input())
words = list(set(input() for _ in range(n)))
print(*sorted(sorted(words), key=lambda x : len(x)), sep='\n')