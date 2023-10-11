n = int(input())
history = set()

answer = 0
for _ in range(n):
    line = input()
    if line == 'ENTER':
        answer += len(history)
        history = set()
    else:
        history.add(line)

print(answer+len(history))