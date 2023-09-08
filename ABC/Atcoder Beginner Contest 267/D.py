N, M = map(int,input().split())
A = list(map(int,input().split()))
dp = [[0]+[-10**30 for _ in range(M)] for _ in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+A[i-1]*j)
print(dp[-1][-1])