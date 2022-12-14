import sys
N = int(sys.stdin.readline())
time = N
while time != 0:
    for i in range(N):
        if (i+1)%2 != 0:
            print('*',end='')
        else:
            print(' ',end='')
    print("")
    for i in range(N):
        if (i+1)%2 == 0:
            print('*',end='')
        else:
            print(' ',end='')
    print("")
    time = time-1