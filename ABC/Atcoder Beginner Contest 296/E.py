def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
def f(a,i):
    if i == 0:
        return a
    else:
        return f(A[a-1],i-1)
"""
感謝の3色上 AC 
ABC 296-E Transition Game
逆から考えるという方法がうまくいきそう
最初 1~N から選べる
周期 1 かつ K_i が存在する閉路が存在している必要がある？
K_i は任意なので周期 2 以上だと確実に負ける
いや、そんなことはないのか
その点が孤立点でなければよい
"""
N = ii()
A = list(miis())
ans = 0
for i in range(N):
    circle_length = set()
    
print(ans)