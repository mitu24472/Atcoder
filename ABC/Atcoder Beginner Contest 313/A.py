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
P = list(miis())
P1 = P[0]
P_other = P[1:]
if N == 1:
    print(0)
else:
    print(max(max(P_other)-P1+1,0))