Burgers = []
Juice = []
for _ in range(3):
    burger = int(input())
    Burgers.append(burger)
Cola = int(input())
Cider = int(input())
Juice.append(Cola)
Juice.append(Cider)
Set_price = min(Burgers) + min(Juice)

print(Set_price-50)