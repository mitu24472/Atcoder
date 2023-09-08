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
    def to_int(self):
        return int(self.x)
def check(i):
    if dp[i]:
        return dp[i]+1
    else:
        return 0
def solve(i):
    if i == N-1:
        ans = decrement
    elif i == N-2:
        ans = decrement*check(i+1) + two_decrement*(dp[i+2]+1) 
    else:
        ans = decrement*check(i+1) + two_decrement*check(i+2)  
    return ans 
N, P = map(int, input().split())
dp = [False for _ in range(N+1)]
dp[-1] = modint(0)
two_decrement = modint(P)/modint(100)
decrement = modint(1) - modint(P)/modint(100)
ans = modint(0)
# 0未満になるときがうまく定義できていない気がする
# dp[0] += two_decrement*(dp[1]+1) かな
# 行くことができない部分を 0 ではない何かで埋めておく必要がある
for i in range(N-1,-1,-1):
    dp[i] = solve(i)
print(dp[1]+1)