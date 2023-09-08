class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (2 * self._size)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._update(i)
    
    def set(self, p, x):
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)
    
    def get(self, p):
        return self._d[p + self._size]

    def prod(self, l, r):
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)
    
    def max_right(self, l, f):
        assert 0 <= l <= self._n
        assert f(self._e())
        if l == self._n: return self._n
        l += self._size 
        sm = self._e()
        while True:
            while l % 2 == 0: l >>= 1
            if not f(self._op(sm, self._d[l])):
                while l < self._size:
                    l <<= 1
                    if f(self._op(sm, self._d[l])):
                        sm = self._op(sm, self._d[l])
                        l += 1
                return l - self._size
            sm = self._op(sm, self._d[l])
            l += 1
            if l & -l == l: break 
        return self._n

    def min_left(self, r, f):
        assert 0 <= r <= self._n
        assert f(self._e())
        if r == 0: return 0
        r += self._size
        sm = self._e()
        while True:
            r -= 1
            while r > 1 and r % 2: r >>= 1 
            if not f(self._op(self._d[r], sm)):
                while r < self._size:
                    r = 2 * r + 1 
                    if f(self._op(self._d[r], sm)):
                        sm = self._op(self._d[r], sm)
                        r -= 1
                return r + 1 - self._size
            sm = self._op(self._d[r], sm)
            if r & -r == r: break
        return 0

    def all_prod(self):
        return self._d[1]

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])
def op(x,y):
    return x+y
def e():
    return 0
def f(x):
    global target
    if x < target:
        return True
    else:
        return False
N = int(input())
A = list(map(int,input().split()))
if (sum(A) // 10) * 10 != sum(A):
    print("No")
    exit()
target = sum(A) // 10
A = A.copy() + A.copy()
A = SegTree(op,e,len(A),A)
for i in range(N):
    ans = A.max_right(i,f)
    if A.prod(i,ans+1) == target:
        print("Yes")
        exit()
print("No")