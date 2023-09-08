N = int(input())
ans = 1
for _ in range(N):
    A = list(map(int,input().split()))
    ans *= sum(A)
    ans %= 10**9 + 7
print(ans)