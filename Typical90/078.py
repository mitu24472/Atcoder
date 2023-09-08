N, M = map(int,input().split())
flag = [0]*N
for _ in range(M):
    a, b = map(int,input().split())
    if a < b:
        flag[b-1] += 1
    else:
        flag[a-1] += 1
ans = 0
for f in flag:
    if f == 1:
        ans += 1
print(ans)