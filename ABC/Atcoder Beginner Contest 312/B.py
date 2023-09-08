def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
def cut_9_9(h,w):
    if N - h < 9 or M - w < 9:
        return
    else:
        ans = []
        for s in S[h:h+9]:
            tmp = []
            for cos in s[w:w+9]:
                tmp.append(cos)
            ans.append(tmp.copy())
        return ans
def check(S):
    if S == None:
        return False
    for s in S[:3]:
        for cos in s[:3]:
            if cos != "#":
                return False
    for s in S[-3:]:
        for cos in s[-3:]:
            if cos != "#":
                return False
    if S[0][3] != "." and S[1][3] != "." and S[2][3] != "." :
        return False
    if S[-1][-4] != "." and S[-2][-4] != "." and S[-3][-4] != ".":
        return False
    if S[3][:4] != [".",".",".","."] and S[-4][-4:] != [".",".",".","."] :
        return False
    return True
N, M = miis()
S  = []
for _ in range(N):
    S.append(input())
ans = []
for h in range(N):
    for w in range(M):
        test = cut_9_9(h,w)
        if check(test):
            ans.append((h,w))
for a in ans:
    print(a[0]+1,a[1]+1)