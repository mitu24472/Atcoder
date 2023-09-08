# dp 典型
def update(i,j):
    global dp
    if (i + j <= N):
        dp[i+j] += dp[i]
    else:
        return 0
N, L = map(int,input().split())
dp = [0 for _ in range(N+1)]
dp[0] = 1
for i in range(N+1):
    update(i,1)
    update(i,L)
print(dp[-1]%(10**9+7))