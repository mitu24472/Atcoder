import sys
from itertools import permutations
sys.setrecursionlimit(1000000)
def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
def solve(per,n,m,ans=[]):
    if len(per) == 1:
        if not("".join(ans+[per[0]]) in T):
            print("".join(ans+[per[0]]))
            exit()
        return 0
    if m == 1:
        for i in range(1,n):
            solve(per[1:],n-i,m-1,ans=ans+[per[0]]+["_"]*i)
    for i in range(1,n-m+2):
        solve(per[1:],n-i,m-1,ans=ans+[per[0]]+["_"]*i)
N,M = miis()
S = [input() for _ in range(N)]
T = {input() for _ in range(M)}
S_sum_length = 0
for s in S:
    S_sum_length += len(s)
if N == 1:
    if S[0] in T:
        print("-1")
    else:
        if len(S[0]) >= 3:
            print(S[0])
        else:
            print("-1")
    exit()
for n in range(max(N-1,3-S_sum_length),16-S_sum_length+2):
    print(n)
    for per in permutations(S,N):
        solve(per,n,N)
print("-1")