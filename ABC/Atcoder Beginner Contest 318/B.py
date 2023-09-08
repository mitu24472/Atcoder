def solve(a,b,c,d):
    global s
    for x in range(a,b):
        for y in range(c,d):
            s.add((x,y))
s = set()
N = int(input())
for _ in range(N):
    a, b ,c ,d = map(int,input().split())
    solve(a,b,c,d)
print(len(s))