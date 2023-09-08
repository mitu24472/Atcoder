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
N = int(input())    
A = list(map(int,input().split()))
B = list(map(int,input().split()))
dp = [[0 for _ in range(3001)] for _ in range(N)]
ruisekiwa = [0 for _ in range(3001)]
for i in range(A[0],B[0]+1):
    dp[0][i] = modint(1)
    ruisekiwa[i] += ruisekiwa[max(i-1,0)] + 1
for i in range(B[0]+1,3001):
    ruisekiwa[i] = ruisekiwa[i-1]
for i in range(1,N):
    ruisekiwa_copy = [0 for _ in range(3001)]
    for j in range(A[i],B[i]+1):
        dp[i][j] = ruisekiwa[j]
        ruisekiwa_copy[j] = (dp[i][j] + ruisekiwa_copy[max(j-1,0)])%mod
    for j in range(B[i]+1,3001):
        ruisekiwa_copy[j] = ruisekiwa_copy[j-1]
    ruisekiwa = ruisekiwa_copy.copy()
print(sum(dp[-1])%mod)