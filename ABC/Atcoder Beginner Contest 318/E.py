# え、 dp やんこんなん
# 添え字を dp[i番目まで見た][i,kの値][0:iだけ選択,1:kまで選択,2:全部選択] とすると、メモリが厳しい
# 2次元 dp として処理すれば ok
# あー、愚直 O(N^2) か
# すべて等しい場合考えたら先にすべて等しいを処理は厳しいな
# dp[i] = Aj = i であるときの組数 とする
# 個数の累積和的な処理をすれば ok? メモリ厳しい
# 
N = int(input().split())
A = list(map(int,input().split()))
dp = [[0 for _ in range(N+1)] for _ in range(3)]
for i,a in enumerate(A):
    for  in range()