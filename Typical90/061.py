from collections import deque
Q = int(input())
card = deque([])
for _ in range(Q):
    t, x = map(int,input().split())
    if t == 1:
        card.appendleft(x)
    elif t == 2:
        card.append(x)
    else:
        print(card[x-1])