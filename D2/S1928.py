import base64
#1928. Base64 Decoder
T = int(input())
for tc in range(1, T+1):
    txt = base64.b64decode(input().strip())
    print('#{} {}'.format(tc, str(txt)[2:-1]))