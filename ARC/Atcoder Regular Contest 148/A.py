import math
import functools
def my_gcd(*integers):
    return functools.reduce(math.gcd, integers)
N = int(input())
A = list(map(int, input().split()))
new_A = []
for i in range(N-1):
    new_A.append(abs(A[i]-A[2]))
if my_gcd(*new_A) == 0 or my_gcd(*new_A) != 2:
    print(1)
else:
    print(2)
