import math
a, b = map(int,input().split())
ans = math.lcm(a,b)
if ans > 10**18:
    print("Large")
else:
    print(ans)