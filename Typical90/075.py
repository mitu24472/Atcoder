N = int(input())
soinsuu = 0
sosuu = []
for i in range(2,int(N**(1/2)+10)):
  while N%i == 0:
    N //= i
    soinsuu += 1
if N != 1:
  soinsuu += 1
ans = 0
while soinsuu > 2**ans:
  ans += 1
print(ans)