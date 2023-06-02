for t in range(int(input())):
    n=int(input())
    number=[0]+list(map(int,input().split()))
    for i in range(1,n+1):
        number[i]+=number[i-1]
    answer=-float('inf')
    for i in range(n+1):
        for j in range(i+1, n+1):
            answer=max(answer,number[j]-number[i])
    print(answer)
            
