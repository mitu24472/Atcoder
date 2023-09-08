M = int(input())
D = list(map(int,input().split()))
year = [1]
mid = (sum(D)+1)//2
for d in D:
    year += [0] * d + [1]
month = 0
day = 0
i = 0
for y in year:
    if  y == 1:
        month += 1
        day = 0
    else:
        i += 1
        day += 1
    if i == mid:
        print(month,day)