Total = int(input())
for _ in range(9):
    price = int(input())
    result = Total - price
    Total = result
print(result)