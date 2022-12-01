T = int(input())
result = []
for _ in range(T):
    A, B = map(int,input().split())
    result.append([A,B])

i=1
for A,B in result:
    print("Case #",end='')
    print(i,end='')
    print(":",end=' ')
    print(A,end=' ')
    print("+",end=' ')
    print(B,end=' ')
    print("=",end=' ')
    print(A+B)
    i = i+1