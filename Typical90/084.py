N = int(input())
S = list(input())
ans = N*(N-1)//2
old = S[0]
length = 1
for s in S[1:]:
    if old != s:
        ans -= (length)*(length-1)//2
        length = 1
        old = s
    else:
        length += 1
ans -= (length)*(length-1)//2
print(ans)