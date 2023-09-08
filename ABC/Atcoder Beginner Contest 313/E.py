def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
# うーんなるほど
# dp とかで行けたりしますか
# 頭意外が 1 でないと不可能とか
# あーそれっぽい
N = ii()
S = list(input())
flag = False
ans = 0
i = -1
non_out_one_count = False
for s in S[1:]:
    if s != "1":
        if flag:
            non_out_one_count = 1
            print(-1)
            exit()
        flag = True
        ans += int(s[i])
    else:
        flag = False
    i += 1
print((ans+non_out_one_count)%998244353)