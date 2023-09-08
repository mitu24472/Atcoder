import bisect
ans = 0
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
A.sort()
for _ in range(Q):
    b = int(input())
    ind = bisect.bisect(A,b)
    if ind-1 < 0:
        print(abs(b-A[ind]))
    elif ind >= len(A):
        print(abs(b-A[ind-1]))
    else:
        print(min(abs(b-A[ind-1]),abs(b-A[ind])))