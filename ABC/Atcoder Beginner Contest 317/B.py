N = int(input())
A = list(map(int,input().split()))
A.sort()
ans = [i for i in range(A[0],A[0]+N+1)]
for an,a in zip(ans,A):
    if an != a:
        print(an)
        exit()