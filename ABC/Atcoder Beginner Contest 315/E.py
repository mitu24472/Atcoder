# こういうのって BFS に帰着できそうですが
# 下っていくから厳しいか
# 再帰かな 深さを持ちつつ
# あー、確かに
import sys
sys.setrecursionlimit(1000000)
def solve(i,d):
    global cost
    global flag
    ans.append((i,d))
    tmp = []
    for c in cost[i]:
        if flag[c-1]:
            flag[c-1] = False
            tmp.append(c-1)
    for t in tmp:
        solve(t,d+1)
ans = []
N = int(input())
cost = [[] for _ in range(N)]
for i in range(N):
    c, *l = map(int,input().split())
    cost[i].extend(l)
max_d = 0
flag = [True] * N
flag[0] = False
solve(0,0)
tmp = []
print(sorted(ans, key=lambda x: x[1]))
for a in list(sorted(ans, key=lambda x: x[1]))[1:]:
    tmp.append(a[0]+1)
print(*tmp[::-1])