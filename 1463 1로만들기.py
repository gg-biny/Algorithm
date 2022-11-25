# N = int(input())
# count = 0
# while N > 1:
#     if N % 3 == 0:
#         N = N/3
#         count += 1
#     elif N % 2 == 0:
#         N = N/2
#         count += 1
#     else:
#         N = N-1
#         count += 1

    

# print(count)


n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])

'''우리는 경로에는 관심이 없고 최소 횟수에만 관심이 있다.'''