def check(x):
    for i in range(3,int(x**0.5)+1):
        if x%i==0: return False
    return True

def sol():
    n=int(input())
    answer=[2,3,5,7]
    for i in range(n-1):
        nxt=[]
        while answer:
            now=answer.pop()
            for i in (1,3,7,9):
                if check(10*now+i):
                    nxt.append(10*now+i)
        
        answer=nxt
    answer.sort()
    for x in answer:print(x)
    
sol()
