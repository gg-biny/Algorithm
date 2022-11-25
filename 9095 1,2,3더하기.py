'''1,2,3 만으로 수 나타내기

4를 표현하는 방법 횟수는
"(3을 표현하는 방법수) + 1" + "(2 표현하는 방법수) + 2" + "(1) + 3 " 이다

그럼 n을 표현하는 방법 횟수는
"(n-1 표현하는 방법수) +1" + "(n-2 표현하는 방법수) + 2" + "(n-3 표현하는 방법수) + 3"

--> 피보나치와 비슷...
'''

T = int(input())

calculate_123 = [-1] * 11
calculate_123[0] = 0
calculate_123[1] = 1
calculate_123[2] = 2
calculate_123[3] = 4

for i in range(4, 11):
    calculate_123[i] = calculate_123[i-1] + calculate_123[i-2] + calculate_123[i-3]

for _ in range(T):
    N = int(input())
    print(calculate_123[N])