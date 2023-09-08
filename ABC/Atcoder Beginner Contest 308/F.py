N, M = map(int, input().split())
P = list(map(int, input().split()))
L = list(map(int, input().split()))
D = list(map(int, input().split()))
LD = []
for l,d in zip(L,D):
    LD.append((l,d))
LD.sort(reverse=True)
print(LD)
P.sort(reverse=True)
