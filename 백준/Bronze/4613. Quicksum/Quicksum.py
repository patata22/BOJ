while True:
    x=input()
    if x=='#':break
    answer=0
    for i in range(len(x)):
        if x[i]==' ': continue
        answer+=(ord(x[i])-64)*(i+1)
    print(answer)
    
