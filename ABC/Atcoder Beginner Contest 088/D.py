from collections import deque
def is_inside(h,w):
    if h < 0 or h >= H or w < 0 or w >= W:
        return False
    else:
        return True
def longest_BFS(s,e,g):
    flag = [True] * len(g)
    flag[s] = False
    next = deque([s])
    i = 0
    while next:
        all_next = next.copy()
        next = deque()
        while all_next:
            v = all_next.pop()
            for j in g[v]:
                if j == e:
                    return i
                if not flag[j]:
                    continue
                else:
                    flag[j] = not flag[j]
                    next.append(j)
        i += 1
    return None
H, W = map(int,input().split())
S = [list(input()) for _ in range(H)]
coun = 0
for s in S:
    for c in s:
        if c == "#":
            coun += 1
G = [[] for _ in range(H*W)]
dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
for h,s in enumerate(S):
    for w,c in enumerate(s):
        if c == '#':
            continue
        else:
            for d in dxdy:
                if is_inside(h+d[0],w+d[1]) and S[h+d[0]][w+d[1]] == '.':
                    G[h*W+w].append((h+d[0])*W+w+d[1])
ans = longest_BFS(0,H*W-1,G)
if ans is None:
    print(-1)
else:
    print(H*W-ans-coun-2)