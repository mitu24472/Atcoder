import math
def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
mod = 998244353
# modint 借用
class modint:
    def __init__(self, x):
        self.x = x % mod
 
    def __str__(self):
        return str(self.x)
 
    __repr__ = __str__
 
    def __add__(self, other):
        return (
            modint(self.x + other.x) if isinstance(other, modint) else
            modint(self.x + other)
        )
 
    def __sub__(self, other):
        return (
            modint(self.x - other.x) if isinstance(other, modint) else
            modint(self.x - other)
        )
 
    def __mul__(self, other):
        return (
            modint(self.x * other.x) if isinstance(other, modint) else
            modint(self.x * other)
        )
 
    def __truediv__(self, other):
        return (
            modint(
                self.x * pow(other.x, mod - 2, mod)
            ) if isinstance(other, modint) else
            modint(self.x * pow(other, mod - 2, mod))
        )
 
    def __pow__(self, other):
        return (
            modint(pow(self.x, other.x, mod)) if isinstance(other, modint) else
            modint(pow(self.x, other, mod))
        )
 
    __radd__ = __add__
 
    def __rsub__(self, other):
        return (
            modint(other.x - self.x) if isinstance(other, modint) else
            modint(other - self.x)
        )
 
    __rmul__ = __mul__
 
    def __rtruediv__(self, other):
        return (
            modint(
                other.x * pow(self.x, mod - 2, mod)
            ) if isinstance(other, modint) else
            modint(other * pow(self.x, mod - 2, mod))
        )
 
    def __rpow__(self, other):
        return (
            modint(pow(other.x, self.x, mod)) if isinstance(other, modint) else
            modint(pow(other, self.x, mod))
        )
 
def ExEuclid(a,b):
    a %= b
    if a == 0: return b, 0
    s, t = b, a
    m0, m1 = 0, 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0
    if m0 < 0: m0 += b // s
    return s, m0
def Chinese_rem(r, m):
    n = len(r)
    r0, m0 = 0, 1 
    for i in range(n):
        r1, m1 = r[i] % m[i], m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1: return [0, 0]
            continue
        g, im = ExEuclid(m0, m1)
        if (r1 - r0) % g: 
            return [0, 0]
        u1 = m0 * m1 // g
        r0 += (r1 - r0) // g * m0 * im % u1
        m0 = u1
    return [r0, m0]
"""
とりあえず CRT と mint をぺたり
1 to 
x = a + kb (mod c+kd)
が存在するか？
愚直厳しそう ← 流石に明らか
"""
N, a, b, c, d = miis()
if math.gcd(c,d) != 1:
    print("-1")
    exit()
r = []
l = []
for i in range(N):
    tmp = Chinese_rem([a+i*b],[c+i*d])
    r.append(tmp[0])
    l.append(tmp[1])
print(Chinese_rem(r,l))