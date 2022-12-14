import sys
modular_42 =[]
for _ in range(10):
    N = int(sys.stdin.readline())
    modular_42.append(N%42)
modular_42 = list(set(modular_42))
print(len(modular_42))