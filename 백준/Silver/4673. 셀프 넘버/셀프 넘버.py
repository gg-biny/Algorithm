numset = set(range(1,10001))
generating_set=set()

for i in range(1,10001):
    for j in str(i):
        i = i + int(j)
    generating_set.add(i)

selfnum = sorted(numset-generating_set)
for x in selfnum:
    print(x)