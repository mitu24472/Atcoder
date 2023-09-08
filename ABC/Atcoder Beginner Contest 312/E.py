def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")

cubes = []
"""
それぞれ持つ面を考える、
対角線とその条件から六つの面は簡単に列挙できる
ちょっと考えます 普通に差を取ればよいのか
((x1,y1,z1),(x2,y2,z2),(x3,y3,z3),(x4,y4,z4)) として情報を持つ
それの共有判定をどのように定めるべきか
↑無理ゲー？
とりあえず列挙だけはします
"""
N = ii()
XYZlist = [tuple(miis()) for i in range(N)]
for x1,y1,z1,x2,y2,z2 in XYZlist:
    # ここに処理
    print("hogehoge")