from collections import defaultdict
def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
# 不変量に着目したいですね
# そんなことはない？ 生成可能列は 1 づつ 単調増加であるような部分を取り除けば
# 生成可能列になるはず → 最初の数配置でなければならない
# 生成可能列が埋め込まれた数を考えたい 1 の数が明らかにそこまでで埋め込まれた生成可能列
# したがって 1 の数を前から数えつつ、 +1 でない時に その数 -1
# 最後まで捜査して、最後に 0 で無いのならば。それは生成可能列でない
# dp によってうまく扱いたい
# dp[i番目まで見た][余剰な 1 の数] とする
# for i in range(len(A)):
#       if A_i != 1:
#           if A_i - A_(i-1) != 1:
#               for j in range(5*10**5+2): 
#                  dp[i][j] = dp[i-1][j+1]
#            else:
#                  dp[i][j] = dp[i-1][j]
#       else:
#           for j in range(1,5*10**5+2):
#              dp[i][j] = dp[i-1][j-1]
#           dp[i][0] = 1
# として、 sum(dp[i][0]) が答え
# 1 の場合はそこで終わっているとみることもできるし、そうしないこともできる
# 1 2 1 をどう処理する？
# 1 で一通り, (1,2) で一通り (1,2,1) で一通り
# 1 ←余剰でない 1,2 ← 余剰でない
# 1,2,1 ← 下がったのだから余剰でないとみることもできる
# 1,2,1,3 みたいなのをどう処理するか
# 厳しくて草、やめます
# 最後の値を保持しておく
# dp[i番目まで見た][余分な1の数][最後の値] こういうの保持不可能 list は hashable でないので
# 最後の値を上手く処理したいですねの気持ちに
N = ii()
A = list(miis())
c = A.count(1)
dp = [[dict() for _ in range(c+1)] for i in range(len(A)+1)]
if A[0] == 1:
    dp[0][0][(1)] = 1
for i in range(len(A)):
    for j in range(c+1):
        if A[i] != 1:
            if A[i] - A[i-1]!= 1:
                for k,item in dp[i-1][j].items():
                    if k[-1] != A[i]+1:
                        dp[i][j] = [dict() for _ in range(c+1)]
                    else:
                        dp[i][j]
            else:
                print(A)
ans = 0
for d in dp:
    ans += d[0]
print(ans)
                