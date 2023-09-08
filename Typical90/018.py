import math
def dist(t):
    return math.sqrt(X**2+(-Y+math.cos(-math.pi/2-t/T*2*math.pi)*L/2)**2)
T = int(input())
L, X, Y = map(int,input().split())
for _ in range(int(input())):
    E = int(input())
    d = dist(E)
    print(math.degrees(math.atan((math.sin(-math.pi/2-E/T*2*math.pi)*L/2+L/2)/d)))