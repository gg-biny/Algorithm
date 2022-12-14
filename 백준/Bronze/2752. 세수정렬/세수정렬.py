import sys
abc_list = list(map(int,sys.stdin.readline().split()))
abc_list.sort()
for c in abc_list:
    print(c,end=' ')