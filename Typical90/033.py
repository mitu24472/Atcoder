H, W = map(int,input().split())
if H == 1 or W == 1:
    print(max(H,W))
    exit()
print((H + H%2)//2 * (W + W%2)//2)