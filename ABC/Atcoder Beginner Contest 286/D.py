def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
N,X = miis()
dp = [False]*(X+1)
dp[0] = True
for i in range(N):
    a,b = miis()
    True_set = set()
    for n,d in enumerate(dp):
        if d:
            for j in range(1,b+1):
                if n+a*j > X:
                    break
                True_set.add(n+a*j)
    for t in True_set:
        dp[t] = True
if dp[X]:
    print("Yes")
else:
    print("No")