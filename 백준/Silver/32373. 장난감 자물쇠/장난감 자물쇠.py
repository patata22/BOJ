def sol():
    n,k=map(int,input().split())
    number=list(map(int,input().split()))
    answer=[0]*n
    for i in range(k):
        temp=[]
        for j in range(i,n,k):
            temp.append(number[j])
        temp.sort(reverse=True)    
        for j in range(i,n,k):
            answer[j]=temp.pop()
    for i in range(n):
        if answer[i]!=i: return 'No'
    return 'Yes'
    
print(sol())