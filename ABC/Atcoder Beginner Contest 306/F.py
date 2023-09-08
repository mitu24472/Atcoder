import bisect,random
def f(Si,Sj):
    ans = 0
    C = Si.copy()
    C.extend(Sj)
    C.sort()
    # O(MlogM)
    for s in Si:
        ans += bisect.bisect(C,s)
    return ans
def guchoku(N,M,S):
    ans = 0
    # O(N^2Mlog(M))
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ans += f(S[i],S[j])
    return ans
N, M = map(int,input().split())
S = [[j+1 for j in range(n*M,(n+1)*M)] for n in range(1,N+1)]
print(guchoku(N,M,S))