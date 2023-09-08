mod = 998244353
def miis():
    return map(int,input().split())
def ii():
    return int(input()) 
def judge(a):
    if a:
        print("Yes")
    else:
        print("No")
def Catalan_num(n):
    return (fact[2*n]*fact_inv[n])%mod * fact_inv[n] % mod * pow(n+1,mod-2,mod) % mod
fact = [1]
for i in range(1,6003): 
    fact.append(fact[-1]*i)
fact_inv = [pow(f,mod-2,mod) for f in fact]
inv = [pow(i,mod-2,mod) for i in range(1,6003)]
S = input()
"""
そうでない括弧列の数え上げに帰着したい 
dp で前から見ていっても解けたりしますか
dp[i番目の文字][現在の座標がj]
とし、遷移を
dp[i+1][j] = dp[i][j-1] + dp[i][j+1]
と定義する
"""
dp = [[0 for _ in range(3003)] for i in range(len(S)+1)]
dp[0][0] = 1
for i,s in enumerate(S):
    i += 1
    for j in range(3003):
        if s == ")":
            if j == 0:
                dp[i][j] += dp[i-1][j+1] % mod
            else:
                if j == 3002:
                    continue
                else:
                    dp[i][j] += dp[i-1][j+1] % mod
        elif s == "(":
            if j == 0:
                continue
            else:
                dp[i][j] = dp[i-1][j-1] % mod
        else:
            if j == 0:
                dp[i][j] = dp[i-1][j+1] % mod
            else:
                if j == 3002:
                    continue
                else:
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
print(dp[-1][0])
        
