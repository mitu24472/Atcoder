from collections import deque
N, Q = map(int,input().split())
d = deque(list(map(int,input().split())))
for _ in range(Q):
    T, x, y = map(int,input().split())
    if T == 1:
        d[x-1], d[y-1] = d[y-1], d[x-1]
    elif T == 2:
        d.rotate()
    else:
        print(d[x-1])