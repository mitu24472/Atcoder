def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
"""
仮定として、 y > max(B) である必要がある
A_i + x = B_i (mod y) であるとき、
任意の i に対して、ある k,l がそんざいして k(A_i+x) = l(B_i) である。
A_i + x = B_i (y1y2...)
13 8 10 11 mod 30 !?
7 2 4 5
3 3 5 0
mod 5, +3
0 0 2 3
mod 6, +3
3 3 5 0
[1,2,3,4,...,y]
のやつを考える
操作は これを x 回 rotate することに等しい
できるだけ一発で揃えられるような物を考える
結局 ある剰余環上で差が B になるような物を構築できるかどうか
それぞれの N を基準にそれとの差を作成する O(N^2) A,Bともに
できるだけ一致している物を基準に rotate これをどうするか厳しいな
"""
A = [7,2,4,5]
B = [3,3,5,0]
for i in range(1,10**5):
    for j in range(1,10**5):
        tmp = []
        for a in A:
            tmp.append((a+j)%i)
        if tmp == B:
            print("x:",j,"Mod:",i)