for _ in range(int(input())):
    answer=0
    a,b,k=map(int,input().split())
    for i in range(a):
        for j in range(b):
            if i&j<k:
                answer+=1      
    print(f'Case #{_+1}: {answer}')