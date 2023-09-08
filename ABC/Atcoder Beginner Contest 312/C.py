def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
def cheak(mid):
    buy_ok = 0
    uru_ok = 0
    for i in range(N):
        if A[i] <= mid:
            uru_ok += 1
    for i in range(M):
        if B[i] >= mid:
            buy_ok += 1
    if uru_ok >= buy_ok:
        return True
    else:
        return False
# 決め打ち二分探索？
N, M = miis()
A = list(miis())
B = list(miis())
ok = 10**9+1
ng = 0
while abs(ng - ok) != 1:
    mid = (ok + ng) // 2
    if cheak(mid):
        ok = mid
    else:
        ng = mid
print(max(ok,ng))