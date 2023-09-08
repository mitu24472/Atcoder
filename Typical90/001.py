# 決め打ちにぶたん？
def meguru_nibutan(ok,ng,f):
    while abs(ok-ng) != 1:
        mid = (ok+ng)//2
        if f(mid):
            ok = mid
        else:
            ng = mid
    if f(ng):
        return ng
    else:
        return ok
def solve(lim):
    cout = 0
    now = 0
    for i,b in enumerate(B):
        now += b
        if now >= lim and i != N and cout != K:
            now = 0
            cout += 1
    if cout >= K and now >= lim :
        return True
    else:
        return False
N, L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))
B = [A[0]]
for i in range(N-1):
    B.append(A[i+1]-A[i])
B.append(L-A[-1])
print(meguru_nibutan(0,L+1,solve))