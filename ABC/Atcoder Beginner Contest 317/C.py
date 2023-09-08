def solve(sumi_set,now,length):
    ans = -10000
    sumi_set.add(now)
    flag = True
    for g in G[now]:
        if not(g[0] in sumi_set):  
            ans = max(solve(sumi_set.copy(),g[0],length+g[1]),ans)
            flag = False
    if flag:
        return length
    return ans
N, M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int,input().split())
    G[a-1].append((b-1,c))
    G[b-1].append((a-1,c))
ans = 0
for i in range(N):
    sumi_set = set()
    ans = max(solve(sumi_set,i,0),ans)
print(ans)