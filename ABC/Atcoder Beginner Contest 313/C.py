import bisect
def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
# 不変量に着目する、総和は sum(A) でかわらない
# つまり sum(A)%N : N - sum(A)%N で配置することになるはず
# プラス方向とマイナス方向で考えていく
# マイナスが大きい方に優先的に できる
# ソートして前後ろから考えていく
N = ii()
A = list(miis())
ans = []
sum_A = sum(A)
A.sort()
for i in range(N-sum(A)%N):
    ans.append(sum_A//N)
for i in range(sum(A)%N):
    ans.append(sum_A//N+1)
max_plus = sum(A)%N
minus = A[:N-sum_A%N]
plus = A[N-sum_A%N:]
print(minus,sum(minus),plus,sum(plus))
test1 = bisect.bisect_right(A,sum_A//N)
test1 = A[:min(test1,N-sum_A%N)]
test2 = bisect.bisect_left(A,sum_A//N+1)
test2 = A[max(test2,N-sum_A%N):]
print(len(test1)*sum_A//N - sum(test1),sum(test2) - len(test2)*(sum_A//N+1))
left = - (len(test1)*sum_A//N - sum(test1) - sum(test2) + len(test2)*(sum_A//N+1))
ans = 0
ans += min(len(test1)*sum_A//N - sum(test1),sum(test2) - len(test2)*(sum_A//N+1))
if left <= 0:
    tmp = 0
    for a in A[min(bisect.bisect_right(A,sum_A//N),N-sum_A%N):max(bisect.bisect_left(A,sum_A//N+1),N-sum_A%N)]:
        tmp += a - sum_A//N
    print(ans+min(tmp,left)+abs(tmp-left))
elif left > 0:
    tmp = 0
    for a in A[min(bisect.bisect_right(A,sum_A//N),N-sum_A%N):max(bisect.bisect_left(A,sum_A//N+1),N-sum_A%N)]:
        tmp += sum_A//N+1 - a
    print(ans+min(tmp,abs(left))+abs(tmp-abs(left)))