s = input()
alphabet = [-1]*26
for i in range(len(s)):
    if alphabet[ord(s[i])-97] == -1:
        alphabet[ord(s[i])-97] = i
print(*alphabet)