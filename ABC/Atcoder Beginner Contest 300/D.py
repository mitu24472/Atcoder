def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
#Gary L.Miller/Michael Rabin(1975) 
#十分小さいN(<3*10**14)について O((logn)**3) 繰り返し二乗法によって O((logn)**2)
#pythonのpowは勝手に繰り返し二乗法を使ってくれる
import math
def Miller_Rabin(N):
    if N <= 1:
        return False
    k = 0
    m = N - 1
    while m & 1 == 0:
        k += 1
        m >>= 1
    assert(2**k*m == N-1)
    task = [2,3,5,7,11,13,17]
    def test(N,t):
        b = pow(t,m,N)
        if b == 1:
            return True
        for i in range(0,k):
            if b == N - 1:
                return True
            b = pow(b,2,N)
        return False
    for t in task:
        if t >= N:
            break
        if not test(N,t):
            return False
    return True
""" 考察スペース
2乗を列挙する
b を愚直に考えても足りるのでは
"""
N = ii()
square_list = [i for i in range(math.floor(math.sqrt(N))) if Miller_Rabin(i)]
count = 0
for i in range(len(square_list)):
    for j in range(i+1,len(square_list)):
        if square_list[i] ** 2 * square_list[j] > N :
            break
        for k in range(j+1,len(square_list)):
            if square_list[i]**2 * square_list[j] * square_list[k] ** 2 > N:
                break
            count += 1
print(count)