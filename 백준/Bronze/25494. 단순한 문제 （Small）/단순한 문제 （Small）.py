for _ in range(int(input())):
    a,b,c=map(int,input().split())
    answer=0
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                if i%j==j%k==k%i:answer+=1
    print(answer)
