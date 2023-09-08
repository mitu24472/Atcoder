"""
DP だと分かったらさすがに終わる
dp[i番目まで見た][獲得者数n人] = 最小のコスト
"""
N = int(input())
dp = [[0]+[10**12 for _ in range(10**5)] for _ in range(N+1)]
x_win = 0
y_win = 0
costs = [(0,0)]
for _ in range(N):
    x, y, z = map(int,input().split())
    if x < y:
        y_win += z
        costs.append(((y-x+1)//2,z))
    else:
        x_win += z
        costs.append((0,z))
if x_win > y_win:
    print(0)
    exit()
for i in range(1,N+1):
    for j in range(10**5+1):
        if j-costs[i][1] >= 0:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-costs[i][1]]+costs[i][0])
        else:
            dp[i][j] = dp[i-1][j]
ans = 10**12
for d in dp:
    ans = min(d[(x_win+y_win+1)//2:])
print(ans)