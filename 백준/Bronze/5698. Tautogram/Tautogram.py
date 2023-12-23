while True:
    answer='Y'
    n=list(map(lambda x:x.lower(),input().split()))
    if n[0]=='*':break
    for x in n:
        if x[0]!=n[0][0]:answer='N'
    print(answer)
