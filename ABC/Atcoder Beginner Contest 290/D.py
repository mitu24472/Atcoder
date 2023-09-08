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
T = ii()
for _ in range(T):
    N,D,K = miis()
    print(math.floor((K-1)/N)+((K-1)*D)%N)