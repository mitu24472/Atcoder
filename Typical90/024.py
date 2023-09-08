# abs が K と 二の倍数差あれば ok
N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
diff = 0
for a,b in zip(A,B):
    diff += abs(b-a)
print("Yes" if K >= diff and (K - diff)%2 == 0 else "No")