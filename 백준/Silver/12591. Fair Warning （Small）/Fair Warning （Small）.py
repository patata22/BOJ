def gcd(x,y):
    while y:x,y=y,x%y
    return x

for tt in range(int(input())):
    
    temp=list(map(int,input().split()))
    n=temp[0]
    number=sorted(temp[1:])            
    diff=[]
    for i in range(1,len(number)):
        diff.append(number[i]-number[i-1])

    answer=diff[0]
    for x in diff:
        answer=gcd(answer,x)
    print(f'Case #{tt+1}: {-number[0]%answer}')
    
