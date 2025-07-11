def check(x):
    if x<=seats[0]-d: return x
    for i in range(1,len(seats)):
        prev=seats[i-1]
        now=seats[i]
        temp=max(prev+d,x)
        if prev+d<=temp<=now-d:return temp
    return max(x,seats[-1]+d)

n,d=map(int,input().split())
number=list(map(int,input().split()))[::-1]
seats=[number.pop()]
answer=[seats[-1]]
while number:
    result=check(number.pop())
    answer.append(result)
    seats.append(result)
    seats.sort()

print(*answer)
    
