# D/P より高いものの集合を用意 ギリギリとそうでない場合を比較
N, D, P = map(int,input().split())
over_dp = []
non_over = []
all = []
tmp = list(map(int,input().split()))
for t in tmp:
    if P/D < t:
        over_dp.append(t)
    else:
        non_over.append(t)
    all.append(t)
over_dp.sort()
non_over.sort()
all.sort()
ticket = len(over_dp)//D
ans = 10**100
for t in range(ticket-10,ticket+10):
    if t < 0:
        continue
    else:
        ans = min(P*t+sum(all[:max(len(all)-t*D,0)]),ans)
print(ans)