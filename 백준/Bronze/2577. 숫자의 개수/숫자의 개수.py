import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline()) 
C = int(sys.stdin.readline())
multiply_ABC = str(A*B*C)
slice_ABC = []
count_onetonine = [0]*10
for i in range(len(multiply_ABC)):
    slice_ABC.append(int(multiply_ABC[i]))
# print(slice_ABC)
# print(count_onetonine)
for i in slice_ABC:
    for j in range(10):
        if i == j:
            count_onetonine[j] += 1
# print(count_onetonine)
for c in count_onetonine:
    print(c)