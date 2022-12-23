while True:
    x=input().split()
    if x[0]=='#': break
    Cheryl = 0
    Tania = 0
    for a in x:
        if a=='*':
            if Cheryl>Tania: print('Cheryl')
            elif Cheryl<Tania: print('Tania')
            else: print('Draw')
            break
        if a=='A' or int(a)%2: Cheryl+=1
        else: Tania+=1