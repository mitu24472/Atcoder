import bisect
N, M, D = map(int,input().split())
S = list(map(int,input().split()))
A = list(map(int,input().split()))
A.sort()
ans = 0
for s in S:
  ind = bisect.bisect(A,s+D) - 1
  if abs(s - A[ind]) <= D:
    ans = max(s+A[ind],ans)
  if len(A) > ind+1: 
    if abs(s - A[ind+1]) <= D:
      ans = max(s+A[ind+1],ans)
if ans == 0:
  print(-1)
else:
  print(ans)
