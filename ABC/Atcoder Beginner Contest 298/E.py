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
N, A, B, P, Q = map(int, input().split())
aoki = [0 for  _ in range(N+1)]
takahashi = [0 for  _ in range(N+1)]
aokidp = [[0 for _ in range(N+1)] for _ in range(N+1)]
takahashidp = [[0 for _ in range(N+1)] for _ in range(N+1)]
takahashidp[0][A] = modint(1)
aokidp[0][B] = modint(1)
takahashi_seni = modint(1)/modint(P)
aoki_seni = modint(1)/modint(Q)
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,P+1):
            takahashidp[i][min(j+k,N)] += takahashi_seni*takahashidp[i-1][j]
    takahashi[i] = takahashi[i-1] + takahashidp[i][N]*(modint(1)-aoki[i-1])*(modint(1)-aoki[i-1]-takahashi[i-1])
    for j in range(1,N+1):
        for k in range(1,Q+1):
            aokidp[i][min(j+k,N)] += aoki_seni*aokidp[i-1][j]
    aoki[i] = aoki[i-1] + aokidp[i][N]*(modint(1)-takahashi[i])*(modint(1)-takahashi[i]-aoki[i-1])
    print(takahashi[i],aoki[i])