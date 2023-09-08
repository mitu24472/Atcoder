from collections import defaultdict
def Miller_Rabin(N):
    if N <= 1:
        return False
    k = 0
    m = N - 1
    while m & 1 == 0:
        k += 1
        m >>= 1
    assert(2**k*m == N-1)
    task = [2,3,5,7,11,13,17,23,29,31,37,43,47]
    def test(N,t):
        b = pow(t,m,N)
        if b == 1:
            return True
        for i in range(0,k):
            if b == N - 1:
                return True
            b = pow(b,2,N)
        return False
    for t in task:
        if t >= N:
            break
        if not test(N,t):
            return False
    return True
def Legendre(A,p):
    row_p = p
    ans = 0
    while A//p != 0:
        ans += A//p
        p *= row_p
    return ans
K = int(input())
ok = K
prime = defaultdict(int)
for i in range(2,int(K**(0.5))+100):
    while K%i == 0:
        K //= i
        prime[i] += 1
ng = 1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    flag = True
    for p in prime.keys():
        if prime[p] > Legendre(mid,p):
            flag = False
    if flag:
        ok = mid
    else:
        ng = mid
print(max(ok,ng))