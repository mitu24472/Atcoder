import bisect
from collections import defaultdict
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
 # https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional
T = TypeVar('T')

class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a: Optional[List[T]] = None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        self.size = len(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __eq__(self, other) -> bool:
        return list(self) == list(other)
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int]:
        "Find the bucket and position which x should be inserted. self must not be empty."
        for a in self.a:
            if x <= a[-1]: break
        return (a, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a, i = self._position(x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a, i = self._position(x)
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
    
    def _pop(self, a: List[T], i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a: self._build()
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a, i = self._position(x)
        if i == len(a) or a[i] != x: return False
        self._pop(a, i)
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError
    
    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return self._pop(a, i)
        else:
            for a in self.a:
                if i < len(a): return self._pop(a, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans
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
    
    def all_prod(self):
        return self._d[1]

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])
def op(x,y):
    return x+y
def e():
    return 0
def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
N = ii()
A = list(miis())
tmp_A = SortedMultiset([])
A_segtree = SegTree(op,e,N)
sort_A = sorted(A)
zatsu_index = [0]*N
zatsu_dic = defaultdict(int)
for i,a in enumerate(A):
    zatsu = bisect.bisect_left(sort_A,a)
    zatsu_index[i] = zatsu + zatsu_dic[a]
    zatsu_dic[a] += 1
ans = modint(0)
for k in range(0,N):
    ind = tmp_A.index_right(A[k])
    tmp_A.add(A[k])
    A_segtree.set(zatsu_index[k],A[k])
    ans += (2*ind+1)*A[k]
    ans += 2*A_segtree.prod(zatsu_index[k]+1,N)
    print(ans*(modint(1)/modint((k+1)**2)))