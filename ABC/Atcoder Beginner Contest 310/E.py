dic = {(0,1):1,(1,0):1,(0,0):1,(1,1):0}
N = int(input())
S = list(map(int,list(input())))
zero_one = [0,0]
zero_one[S[0]] += 1
ans = 0
ans += zero_one[1]
for s in S[1:]:
    if s == 0:
        zero_one[0], zero_one[1] = 1, zero_one[1]+zero_one[0]
        ans += zero_one[1]
    else:
        zero_one[0], zero_one[1] = zero_one[1], zero_one[0]+1
        ans += zero_one[1]
print(ans)