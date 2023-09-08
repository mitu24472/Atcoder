import bisect
def solve(A,i):
    if i == 30:
        return 0
    ind = bisect.bisect(A,2**(30-i))
    one = A[ind:]
    zero = A[:ind]
    if len(one) == 0:

        return solve(A,i+1)
    elif len(zero) == 0:
        return solve(A,i+1)
    else:
        if  2**(30-i)+solve(zero,i+1) < 2**(30-i)+solve(one,i+1):
            return 2**(30-i)+solve(zero,i+1)
        else:
            return 2**(30-i)+solve(one,i+1)

N = int(input())
A = list(map(int,input().split()))
A.sort()
print(solve(A,0))