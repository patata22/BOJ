while True:
    lst1=[]
    lst2=[]
    n=int(input())
    if n==0:break
    else:
        n=str(n)
        for i in range(int((len(n)//2))):
            lst1.append(n[i])
            lst2.append(n[-i-1]) 
    if lst1==lst2:
        print("yes")
    else:
        print("no")