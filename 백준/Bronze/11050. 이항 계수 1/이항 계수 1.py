n,k = map(int,input().split())
Bunmo1 = 1
Bunmo2 = 1
Bunja = 1

for i in range(1,n+1):
    Bunja *= i
for j in range(1,k+1):
    Bunmo1 *= j
for l in range(1,n-k+1):
    Bunmo2 *= l

answer = int(Bunja / (Bunmo1 * Bunmo2))
print(answer)
            