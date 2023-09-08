cubic_num = set()
for i in range(1,int((2*10**11)**(1/3))+1):
    cubic_num.add(i**3)
N, Q = map(int, input().split())
A = list(map(int, input().split()))
Querys = [tuple(map(int, input().split())) for _ in range(N)]
