N = int(input())
S = input()
big_S = S.upper()
small_S = S.lower()
S = list(S)
big_S = list(big_S)
small_S = list(small_S)
Q = int(input())
Querys = []
last_change = 0
for q in range(Q):
    t, x, c = input().split()
    Querys.append((int(t),int(x),c))
    if t != "1":
        last_change = q
for i in range(Q):
    if Querys[i][0] != 1:
        if i != last_change:
            continue
        else:
            if Querys[i][0] == 2:
                S = small_S.copy()
            else:
                S = big_S.copy()
    else:
        S[Querys[i][1]-1] = Querys[i][2]
        small_S[Querys[i][1]-1] = Querys[i][2].lower()
        big_S[Querys[i][1]-1] = Querys[i][2].upper()
print("".join(S))