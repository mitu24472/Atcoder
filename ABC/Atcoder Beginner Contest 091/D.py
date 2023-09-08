from bisect import bisect_right, bisect_left
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
BB = [[] for _ in range(30)]
for i in range(30):
    for b in B:
        BB[i].append(B%2**i)
    BB[i].sort()
ans = 0
for i in range(30):
    one_count = 0
    for a in A:
        if a & (1 << i):
            one_count += N - bisect_left(BB[i],2**i - (a-2**i))
            one_count += N - bisect_right()