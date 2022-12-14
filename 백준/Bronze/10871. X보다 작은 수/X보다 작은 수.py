import sys
N, X = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
smallnum =[]
for c in A:
    if c < X:
        smallnum.append(c)
for c in smallnum:
    print(c,end=' ')