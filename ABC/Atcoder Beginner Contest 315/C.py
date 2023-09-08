H, W = map(int,input().split())
S = [input() for _ in range(H)]
ans = []
add_que = []
for s in S:
  T_flag = False
  cans = []
  for cos in s:
    if T_flag and cos == "T":
      add_que = ["P","C"]
      cans.extend(add_que)
      add_que = []
      T_flag = False
    elif cos == "T":
      add_que.append("T")
      T_flag = True
    else:
      add_que.append(cos)
      T_flag = False
      cans.extend(add_que)
      add_que = []
  cans.extend(add_que)
  ans.append(cans)
for a in ans:
  print("".join(a))