H, W = map(int,input().split())
# 各々の列に対して計算
A = [list(map(int,input().split())) for _ in range(H)]
sumW = [sum(A[i]) for i in range(H)]
sumH = []
for i in range(W):
    tmp = 0
    for j in range(H):
        tmp += A[j][i]
    sumH.append(tmp)
for h in range(H):
    tmp = []
    for w in range(W):
        tmp.append(sumH[w]+sumW[h]-A[h][w])
    print(*tmp)