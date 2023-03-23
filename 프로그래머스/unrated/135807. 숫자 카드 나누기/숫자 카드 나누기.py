def solution(arrayA, arrayB):
    answer=0
    
    n=len(arrayA)
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    for i in range(1,n):
        gcdA = gcd(gcdA, arrayA[i])
        gcdB = gcd(gcdB, arrayB[i])
    #if gcd(gcdA, gcdB)!=1: return 0
    candA = []
    candB = []
    for i in range(1,int(gcdA**0.5)+1):
        if not gcdA%i:
            candA.append(gcdA//i)
            candA.append(i)
    for i in range(1,int(gcdB**0.5)+1):
        if not gcdB%i:
            candB.append(gcdB//i)
            candB.append(i)
    candA.sort(reverse=True)
    candB.sort(reverse=True)
    for a in candA:
        dividable=False
        for b in arrayB:
            if not b%a:
                dividable=True
                break
        if not dividable:
            answer=max(a,answer)
            break
    
    for b in candB:
        dividable=False
        for a in arrayA:
            if not a%b:
                dividable=True
                break
        if not dividable:
            answer=max(b,answer)
            break
                
    return answer

def gcd(x,y):
    while y: x,y=y,x%y
    return x