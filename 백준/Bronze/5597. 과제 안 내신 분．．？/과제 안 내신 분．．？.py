attend = []
notatt = []
for i in range(28):
    attend.append(int(input()))
for i in range(1,31):
    if i not in attend:
        notatt.append(i)
print(min(notatt))
print(max(notatt))