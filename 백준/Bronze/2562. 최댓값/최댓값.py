list9 = []
for i in range(9):
    list9.append(int(input()))
m = max(list9)
print(m)
print((list9.index(m))+1)