N, M ,P = map(int,input().split())
s = {M+i*P for i in range(1000000)}
ans = 0
for i in range(1,N+1):
    if i in s:
        ans += 1
print(ans)