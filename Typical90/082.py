L, R = map(int,input().split())
i = 0
ans = 0
while L >= 10**i:
    i += 1
i -= 1
while 10**i <= R:
    ans += (min(R,10**(i+1)-1) + max(L,10**i)) * (min(R,10**(i+1)-1) - max(L,10**i) + 1) * (i+1) // 2
    ans %= 10**9 + 7
    i += 1
print(ans)