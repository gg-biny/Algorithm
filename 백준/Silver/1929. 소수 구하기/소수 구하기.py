
M, N = map(int,input().split())
prime_num=[]
for i in range(M,N+1):
    flag = True
    if i==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            flag = False
            break
    if flag==True:
        prime_num.append(i)

for x in prime_num:
    print(x)
