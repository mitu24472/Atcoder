import sys
sys.setrecursionlimit(1000000)
def solve(now):
    global flag
    global ans
    if (G[now] - flag) & G[now]:
        next = min((G[now] - flag) & G[now])
        flag.add(next)
        ans.append(next+1)
        if not (next in dic_flag):
            dic_flag.add(next)
            frist_city[next] = now
        solve(next)
    elif now == 0:
        return 0
    else:
        next = frist_city[now]
        ans.append(next+1)
        solve(next)
N = int(input())
G = [set() for _ in range(N)]
for _ in range(N-1):
    a, b = map(int,input().split())
    G[a-1].add(b-1)
    G[b-1].add(a-1)
flag = set()
flag.add(0)
dic_flag = set()
frist_city = dict()
ans = [1]
solve(0)
print(*ans)