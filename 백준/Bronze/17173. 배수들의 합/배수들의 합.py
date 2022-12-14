import sys
N, M = map(int,sys.stdin.readline().split())
list_K = list(map(int,sys.stdin.readline().split()))
multi_K=set()
for num in list_K:
    multinum = num
    while multinum <= N:
        multi_K.add(multinum)
        multinum += num

# print(multi_K)
print(sum(multi_K))
