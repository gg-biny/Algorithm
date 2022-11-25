T=int(input())


cnt_fibo = [[0,0] for _ in range(41)]
# 얕은 복사, 깊은 복사 문제로 [0,0] * 41 을 쓰면 오류 발생. 주의

cnt_fibo[0] = [1,0]
cnt_fibo[1] = [0,1]

for _ in range(T):
    N=int(input())
    for i in range(2,N+1):
        cnt_fibo[i][0] = cnt_fibo[i-1][0] + cnt_fibo[i-2][0]
        cnt_fibo[i][1] = cnt_fibo[i-1][1] + cnt_fibo[i-2][1]

    print(cnt_fibo[N][0],end=' ')
    print(cnt_fibo[N][1])
    
# for i in range(2,41):
#     cnt_fibo[i][0] = cnt_fibo[i-1][0] + cnt_fibo[i-2][0]
#     cnt_fibo[i][1] = cnt_fibo[i-1][1] + cnt_fibo[i-2][1]


# for _ in range(T):
#     N=int(input())
#     print(cnt_fibo[N][0],end=' ')
#     print(cnt_fibo[N][1])

#--> 이 방법이 조금 더 빠르다. 