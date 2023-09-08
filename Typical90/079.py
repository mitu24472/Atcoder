def solve(h,w,diff):
    global A
    global ans
    ans += abs(diff)
    A[h][w] -= diff
    A[h+1][w] -= diff
    A[h][w+1] -= diff
    A[h+1][w+1] -= diff
H, W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
B = [list(map(int,input().split())) for _ in range(H)]
ans = 0
for w in range(W-1):
    for h in range(H-1):
        solve(h,w,A[h][w]-B[h][w])
for a,b in zip(A,B):
    for coa,cob in zip(a,b):
        if coa != cob:
            print("No")
            exit()
print("Yes")
print(ans)