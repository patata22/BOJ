def sol():
    a,b=map(int,input().split())
    temp=[]
    while a:
        temp.append(a%b)
        a//=b
    for i in range(len(temp)//2):
        if temp[i]!=temp[-i-1]:return 0
    return 1
    

for _ in range(int(input())):
    print(sol())
