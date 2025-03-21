def gcd(x,y):
    while y:  x,y=y,x%y
    return x

def lcm(x,y):
    return x*y//gcd(x,y)

def sol(start,depth):
    global answer
    if depth==8: return
    for i in range(start+1,7):
        if not used[i]:
            used[i]=1
            result=1
            for j in range(7):
                if used[j]: result=lcm(result,one[j])
            if depth%2: answer+=n//result
            else: answer-=n//result
            sol(i,depth+1)
            used[i]=0           

n=int(input())
prime=[2,3,5,7,11,13,17]
one=[(10**x-1)//9 for x in prime]
used=[0]*7
answer=0

sol(-1,1)

print(answer)