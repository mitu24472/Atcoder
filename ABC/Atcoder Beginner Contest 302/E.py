N, Q = map(int,input().split())
G = [set() for _ in range(N)]
ans = N
for _ in range(Q):
    q, *uv = map(int,input().split())
    if  q == 1:
        if len(G[uv[0]-1]) == 0:
            ans -= 1
        if len(G[uv[1]-1]) == 0:
            ans -= 1
        G[uv[0]-1].add(uv[1]-1)
        G[uv[1]-1].add(uv[0]-1)
    else:
        for g in G[uv[0]-1]:
            G[g].discard(uv[0]-1)
            if len(G[g]) == 0:
                ans += 1
        if len(G[uv[0]-1]) != 0:
            ans += 1
        G[uv[0]-1] = set()
    print(ans)