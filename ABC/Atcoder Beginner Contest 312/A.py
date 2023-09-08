def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
se = set(["ACE","BDF","CEG","DFA","EGB","FAC","GBD"])
S = input()
judge(S in se) 