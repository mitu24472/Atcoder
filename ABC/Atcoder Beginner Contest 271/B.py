N, M = map(int, input().split())
A = list(map(int, input().split()))
# 式が出たのでそれに沿ってやっていく
# 最初だけ愚直に
old_B = A[0]
ans = 0
sum_B = sum(A[:M])
ans_sum_B = 0 
for i in range(1,M+1):
    ans_sum_B += A[i-1]*i
ans = ans_sum_B
for i in range(M,N):
    ans_sum_B = ans_sum_B - sum_B + M*A[i]
    ans = max(ans, ans_sum_B)
    sum_B = sum_B - A[i-M] + A[i]
print(ans)