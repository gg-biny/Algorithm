word = input().upper()
wordset = list(set(word))
countlist = []

for c in wordset:
    n = word.count(c)
    countlist.append(n)

if countlist.count(max(countlist)) >1 :
    print("?")
else:
    print(wordset[(countlist.index(max(countlist)))])
