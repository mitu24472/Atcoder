from itertools import permutations
ans = 10**12
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
t = [i for i in range(N)]
ng_set = set()
M = int(input())
for _ in range(M):
    x, y = map(int,input().split())
    ng_set.add((x-1,y-1))
    ng_set.add((y-1,x-1))
for p in permutations(t):
    tmp = A[0][p[0]]
    oldp = p[0]
    for i,cop in enumerate(p[1:]):
        if (oldp,cop) in ng_set:
            break
        else:
            tmp += A[i+1][cop]
            oldp = cop
    else:
        ans = min(ans,tmp)
if ans == 10**12:
    print("-1")
else:
    print(ans)