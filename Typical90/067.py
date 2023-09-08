def change10(N):
    ans = 0
    for i,n in enumerate(N[::-1]):
        ans += int(n)*8**i
    return ans
def change9(N):
    N = int(N)
    ans = ""
    for i in range(20,-1,-1):
        tmp = N//9**i
        N -= tmp*9**i
        if tmp == 8:
            tmp = 5
        ans += str(tmp)
    return ans
N, K = map(int,input().split())
N = str(N)
for _ in range(K):
    N = change10(N)
    N = change9(N)
print(int(N))
