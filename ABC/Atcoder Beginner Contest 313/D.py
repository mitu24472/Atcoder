def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
# これは総 xor を聞いていることにひとしい
# あー、 K = 1 の最悪ケースがあるのか
# K = 1 ならば、全部に対して聞いていけば、一意に定まる。
# K != 1 でないならば、物理好きさんのものを応用することを考えます
# 初手で A_0 ... A_K を聞き、一つづつスライドしていけば偶奇の組はわかる
# 0 の場所をすべて特定したい
# あー、セグ木の逆みたいなことをすればよい？
# 実装をちゃんとしていないので不可能、悲しい
# K の選び方としてありうるものすべてを考える？
# ターミナルみたいなのはこれでも持てそう
# すべての質問に対して答えを持つにはどうしたら良いか
# 