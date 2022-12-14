N=int(input())
a = N //10
b = N % 10
cycle = 0
new_num = -1
while new_num != N:
    c = a+b
    a = b
    b = c % 10
    new_num = (10*a) + b
    cycle = cycle + 1
print(cycle)
