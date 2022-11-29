T= int(input())

for _ in range(T):
    OXlist = list(input())
    score = 0
    sumscore = 0
    for tf in OXlist:
        if tf == 'O':
            score += 1
            sumscore += score
        else:
            score = 0
    print(sumscore)
