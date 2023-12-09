while True:
    vote=list(input())
    if vote[0]=='#': break
    y,n,N=0,0,0
    for x in vote:
        if x=='Y': y+=1
        elif x=='N': n+=1
        if x!='A':N+=1
    if 2*N<=len(vote):print('need quorum')
    elif y>n: print('yes')
    elif y<n: print('no')
    else:print('tie')
