# 全探索？ 16 は bitdp やれ感がある
N = int(input())

dp = [[float("inf")] * N for _ in range(2**N)]
dist = [[0] * N for _ in range(N)]
for i in range(N-1):
    tmp = list(map(int,input().split()))
    for j,t in enumerate(tmp):
        dist[i][j+i+1] = t
        dist[j+i+1][i] = t
# dp[頂点の集合] = 頂点の集合内部で線を結ぶ方法であって最大のコストのもの
dp = [0 for _ in range(2**N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        dp[2**i+2**j] = dist[i][j]
for s in range(2**N):
    for u in range(N):
        for v in range(N):
            if (not s >> u & 1) and (not s >> v & 1):
                ns = s | 1 << v
                ns = ns | 1 << u
                dp[ns] = max(dp[ns],dp[s]+dist[u][v])
print(max(dp))