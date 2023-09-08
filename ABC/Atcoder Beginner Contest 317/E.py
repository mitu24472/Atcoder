def is_inside(h,w):
    if (0 <= h < H) and (0 <= w < W):
        return True
    else:
        return False
def make_eye(h,w,dxdy):
    global A
    i = 1
    while is_inside(h+dxdy[0]*i,w+dxdy[1]*i) and (A[h+dxdy[0]*i][w+dxdy[1]*i] == "." or A[h+dxdy[0]*i][w+dxdy[1]*i] == "e"):
        A[h+dxdy[0]*i][w+dxdy[1]*i] = "e"
        i += 1
from collections import deque
def BFS(s,g):
    flag = [True] * len(g)
    flag[s] = False
    next = deque([s])
    i = 0
    while next:
        i += 1
        row_next = next.copy()
        next = deque([])
        while row_next:
            v = row_next.popleft()
            for j in g[v]:
                if not flag[j]:
                    continue
                else:
                    if j == g_hw:
                        return i
                    flag[j] = not flag[j]
                    next.append(j)
    return -1
"""
結局侵入できないマスと向いている方向は等しいから
重めの実装をやれば終わる
特殊文字として "e" を実装する これは目線走ってるよ～っていうやつ
"""
H, W = map(int,input().split())
A = [list(input()) for _ in range(H)]
dxdy_dic = {">":(0,1),"<":(0,-1),"v":(1,0),"^":(-1,0)}
for h,a in enumerate(A):
    for w,coa in enumerate(a):
        if coa == "S":
            s_hw = h*W + w
        elif coa == "G":
            g_hw = h*W + w
        elif coa in dxdy_dic.keys():
            make_eye(h,w,dxdy_dic[coa])
for a in A:
    print("".join(a))
G = [[] for _ in range(H*W)]
dxdy = [(0,1),(1,0),(-1,0),(0,-1)]
for h,a in enumerate(A):
    for w,coa in enumerate(a):
        if coa == "." or coa == "S" or coa == "G":
            for d in dxdy:
                if is_inside(h+d[0],w+d[1]):
                    if A[h+d[0]][w+d[1]] == "." or A[h+d[0]][w+d[1]] == "G" or A[h+d[0]][w+d[1]] == "S":
                        G[h*W+w].append((h+d[0])*W+w+d[1])
print(BFS(s_hw,G))