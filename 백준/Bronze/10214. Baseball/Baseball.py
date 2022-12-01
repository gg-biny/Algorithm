T = int(input())
for _ in range(T):
    Yon, Ko = 0,0
    for i in range(9):
        Y,K = map(int,input().split())
        Yon = Yon + Y
        Ko = Ko + K
    if Yon > Ko :
        print("Yonsei")
    elif Yon < Ko :
        print("Korea")
    else:
        print("Draw")