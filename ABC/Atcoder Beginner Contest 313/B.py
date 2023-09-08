def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
#関数実装
# s は始点 g は二次元リスト eは終点
#素の BFS は return していないので必要があれば適当なものを付け足してください
from collections import deque
def BFS(s,g):
    flag = [True] * len(g)
    flag[s] = False
    next = deque([s])
    while next:
        v = next.popleft()
        for j in g[v]:
            if not flag[j]:
                continue
            else:
                flag[j] = not flag[j]
                next.append(j)
    return flag
# グラフを作り、それが全体に対して親が決定できれば良い。
# 0 に対して全ての子が含まれれば 〇
N ,M = miis()
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = miis()
    graph[a-1].append(b-1)
ans = []
for i in range(N):
    flag = BFS(i,graph)
    ok = True
    for f in  flag:
        if f:
            ok = False
    if ok:
        ans.append(i+1)
print(ans)