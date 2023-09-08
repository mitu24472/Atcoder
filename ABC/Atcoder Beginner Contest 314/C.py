from collections import defaultdict
N, M = map(int,input().split())
S = list(input())
C = list(map(int,input().split()))
color_dic = defaultdict(list)
color_dic2 = defaultdict(list)
for i,c in enumerate(C):
    color_dic[c].append((S[i]))
    color_dic2[c].append(i)
for key,lis in color_dic.items():
    color_dic[key] = [color_dic[key][-1]]+color_dic[key][:-1]
ans = ["1" for _ in range(N)]
for key,lis in color_dic.items():
    for i,l in enumerate(lis):
        ans[color_dic2[key][i]] = l
print("".join(ans))