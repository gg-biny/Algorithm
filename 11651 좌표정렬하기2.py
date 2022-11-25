N = int(input())
result = []
for _ in range(N):
    X,Y = (map(int,input().split())) 
    result.append([X,Y])

result.sort(key=lambda x:(x[1],x[0]))

for v in result:
    print(v[0],v[1])