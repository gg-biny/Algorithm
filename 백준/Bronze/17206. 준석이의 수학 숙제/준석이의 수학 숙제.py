import sys
T = int(sys.stdin.readline())
N_list=map(int,sys.stdin.readline().split())
multi_3, multi_7,multi_21 = 0,0,0
result_3,result_7,result_21 = 0,0,0
for v in N_list:
    while multi_3 <= v:
        result_3 = result_3 + multi_3
        multi_3 = multi_3 + 3
    while multi_7 <= v:
        result_7 = result_7 + multi_7
        multi_7 = multi_7 + 7
    while multi_21 <= v:
        result_21 = result_21 + multi_21
        multi_21 = multi_21 + 21
    result = result_3 + result_7 - result_21
    print(result)