N, Q = map(int,input().split())
A = list(map(int,input().split()))
diff = []
ans = 0
for i in range(N-1):
  diff.append(A[i]-A[i+1])
  ans += abs(diff[i])
for _ in range(Q):
  l, r, v = map(int,input().split())
  if l == 1 and r == N:
    print(ans)
    continue
  elif l == 1:
    ans += abs(v+diff[r-1]) - abs(diff[r-1])
    diff[r-1] += v
  elif r == N:
    ans += abs(diff[l-2]-v) - abs(diff[l-2])
    diff[l-2] -= v
  else:
    ans += abs(diff[l-2]-v) - abs(diff[l-2])
    ans += abs(diff[r-1]+v) - abs(diff[r-1])
    diff[l-2] -= v
    diff[r-1] += v
  print(ans)