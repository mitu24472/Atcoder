import math
a, b, c = map(int,input().split())
s = math.gcd(math.gcd(a,b),c)
print(a//s+b//s+c//s-3)