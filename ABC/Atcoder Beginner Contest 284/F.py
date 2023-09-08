import random
base = random.randint(2**31,2**32-1)
mod = 2**32-1
hash_dic = {chr(i+97):i+1 for i in range(26)}
def rolling_hash_0_to_N(S):
    ans = [0,hash_dic[S[0]]]
    old_hash = hash_dic[S[0]]
    for i in range(1,len(S)):
        tmp = (old_hash*base+hash_dic[S[i]])%mod
        ans.append(tmp)
        old_hash = tmp
    return ans
class rolling_hash():
    def __init__(self,S,base=None):
        self.string = S
        if base is None:
            self.baselist = baselist(base,len(S))
        else:
            self.baselist = base
        self.rolling_hash = rolling_hash_0_to_N(S)
    # S(l,r) のハッシュを計算します
    def slice(self,l,r):
        return self.rolling_hash[r] - self.rolling_hash[l] * self.baselist[r-l]
def baselist(base,N):
    ans = [1,base]
    old = base
    for _ in range(N-1):
        ans.append(old*base)
        old *= base
        if old > mod:
            old %= mod
    return ans
N = int(input())
basel = baselist(base,N)
T = rolling_hash(input(),basel)
T_revese = rolling_hash(T.string[::-1],basel)
for i in range(N):
    if (T_revese.slice(i,i+N))%mod == (T.slice(0,N-i)*T.baselist[i]+T.slice(2*N-i,2*N))%mod:
        if T.string[i:i+N] != T_revese.string[0:N-1] + T_revese.string[2*N-i:2*N]:
            continue
        print(T_revese.string[i:i+N])
        print(N-i)
        exit()
print(-1)