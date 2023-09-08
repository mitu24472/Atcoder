S = set()
for i in range(int(input())):
    s = input()
    if s in S:
        continue
    else:
        S.add(s)
        print(i+1)