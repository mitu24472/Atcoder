import copy
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    G[a-1].append((b-1, c))
dist = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0
        else:
            flag = True
            for g in G[i]:
                if g[0] == j:
                    dist[i][j] = g[1]
                    flag = False
            if flag:
                dist[i][j] = 10**12
ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            if dist[i][j] == 10**12:
                continue
            else:
                ans += dist[i][j]
print(ans)