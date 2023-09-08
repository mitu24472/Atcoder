from collections import deque
def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
delate_tuple = []
N = ii()
S = list(input())
left = deque([])
flag = False
ans = []
last = 0
tmp_delate = (10**12,10**12)
for i,s in enumerate(S):
    if s == "(":
        left.append(i)
    elif s == ")":
        if left:
            l = left.pop()
            if  l < tmp_delate[0]:
                tmp_delate = (l,i)
            else:
                delate_tuple.append(tmp_delate)
                tmp_delate = (l,i)
delate_tuple.append(tmp_delate)
ans = []
not_good_set = set()
for l,r in delate_tuple:
    for i in range(l,r+1):
        not_good_set.add(i)
for i,s in enumerate(S):
    if not (i in not_good_set):
        ans.append(s)
print("".join(ans))