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
"""
X に任意の非負整数を append することを繰り返す
両者結局下から詰めていきたいという気持ちに(未証明)
入力例 3 的にダメそう
継ぎ目以下のものを一つ追加すれば ok. もう片方はそれを埋めることに注力するはず
実装不可能で泣いています
BBBAABABA
o    
o    o
oo   o
oo   oo
ooo 
"""
N = ii()
S = list(input())
dic1 = {"A":"Bob","B":"Alice"}
dic2 = {"Alice":"Bob","Bob":"Alice"}
changes = {"A":deque([]),"B":deque([])}
old_s = S[0]
old_s_num = 0
for i,s in enumerate(S[1:]):
    if s != old_s:
        changes[old_s].append(i)
    old_s = s
A_cost = 0
B_cost = 0
if S[0] == "A":
    for s in S:
        if s == "A":
            B_cost += 1
        else:
            break
else:
    for s in S:
        if s == "B":
            A_cost += 1
        else:
            break
win = dic2[dic1[S[0]]]
ans = [1 for _ in range(N)]
for i in range(N):
    flag = True
    if i % 2 == 0:
        if A_cost <= 1:
            flag = False
            print("Alice")
            continue
        if (not B_cost) and changes["B"] and A_cost <= 0:
            win = dic2[win]
            B_cost = changes["B"].pop()
        else:
            A_cost -= 1
    elif i%2 == 1:
        if B_cost <= 1:
            print("Bob")
            flag = False
        if (not A_cost) and changes["A"] and B_cost <= 0:
            win = dic2[win]
            A_cost = changes["A"].pop()
        else:
            B_cost -= 1
    if flag:
        print(win)