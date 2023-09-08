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
ナップザック味を感じる
dp をしたいですが どうすればよい
缶切りを取る数を減らせば、Ti = 0 である中で max のものを一つ増やせる
→ 缶切りが不要な缶をできるだけ取って、余ったら缶切り+ (Ti = 1の品物) をできるだけ取る
もし缶切りが不要な缶 全てを取ることができているのなら、それをmin から二個減らして、缶切りと Ti = 1の品物 max を取る 
↑ multisortedset 以外ありえん tatyam さんの multisortedset、 key 指定がない？
C++ 書くにしても時間なくて草 終わりや
greedy で行ける、考察ミスです...
"""

