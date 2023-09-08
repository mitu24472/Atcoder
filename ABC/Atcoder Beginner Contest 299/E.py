from collections import deque
def BFS_dist(s,g):
    flag = [True] * len(g)
    flag[s] = False
    next = deque([s])
    i = 0
    dist = [0 for _ in range(len(G))]
    while next:
        i += 1
        now_next = next.copy()
        next = deque([])
        while now_next:
            v = now_next.popleft()
            for j in g[v]:
                if not flag[j]:
                    continue
                else:
                    flag[j] = not flag[j]
                    dist[j] = i
                    next.append(j)
    return dist
def BFS_judge(s,g):
    flag = [True] * len(g)
    flag[s] = False
    next = deque([s])
    i = 0
    near_B = 10**12
    if B_W[s] == 1:
        near_B = 0
    while next:
        i += 1
        now_next = next.copy()
        next = deque([])
        while now_next:
            v = now_next.popleft()
            for j in g[v]:
                if not flag[j]:
                    continue
                else:
                    flag[j] = not flag[j]
                    next.append(j)
                    if B_W[j] == 1:
                        near_B = min(near_B,i)
    return near_B
N, M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    v1, v2 = map(int,input().split())
    G[v1-1].append(v2-1)
    G[v2-1].append(v1-1)
K = int(input())
B_W = [1 for _ in range(N)]
dist_G = [BFS_dist(i,G) for i in range(N)]
dist_pd = []
for _ in range(K):
    p, d = map(int,input().split())
    dist_pd.append((p-1,d))
for p,d in dist_pd:
    for n,dis in enumerate(dist_G[p]):
        if dis < d:
            B_W[n] = 0
for p,d in dist_pd:
    if d != BFS_judge(p,G):
        print("No")
        exit()
if not (1 in B_W):
    print("No")
else:
    print("Yes")
    print("".join(list(map(str,B_W))))