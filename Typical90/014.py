# 合計 9999 枚以下の硬貨でちょうど N 円を支払うことができる
# ↑これギャグでしょ 愚直が間に合います
N = int(input())
A, B, C = map(int,input().split())
ans = 10000
for i in range(10000):
    for j in range(10000-i):
        if (N - i*A - j*B)%C == 0:
            ans = min(ans,i+j+(N - i*A - j*B)//C)
print(ans)