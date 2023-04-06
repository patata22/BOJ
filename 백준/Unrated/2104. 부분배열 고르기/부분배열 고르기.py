import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def makeSumSeg(node,s,e):
    if s==e:
        sumTree[node]=number[s]
    else:
        mid=(s+e)//2
        sumTree[node]=makeSumSeg(node*2,s,mid)+makeSumSeg(node*2+1,mid+1,e)
    return sumTree[node]

def makeMinSeg(node,s,e):
    if s==e:
        minTree[node]=s
    else:
        mid=(s+e)//2
        a=makeMinSeg(node*2,s,mid)
        b=makeMinSeg(node*2+1,mid+1,e)
        if number[a]<number[b]:
            minTree[node]=minTree[node*2]
        else: minTree[node]=minTree[node*2+1]
    return minTree[node]

def getSum(node,s,e,l,r):
    if e<l or s>r: return 0
    elif l<=s and e<=r: return sumTree[node]
    else:
        mid=(s+e)//2
        return getSum(node*2, s,mid,l,r)+getSum(node*2+1,mid+1,e,l,r)

def getMin(node,s,e,l,r):
    if e<l or s>r: return -1
    elif l<=s and e<=r: return minTree[node]
    else:
        mid=(s+e)//2
        a=getMin(node*2,s,mid,l,r)
        b=getMin(node*2+1,mid+1,e,l,r)
        if a==-1:return b
        elif b==-1:return a
        elif number[a]<number[b]: return a
        else: return b

def getAnswer(s,e):
    if s==e:
        return number[s]**2
    else:
        pivot = getMin(1,0,n-1,s,e)
        answer = number[pivot] * getSum(1,0,n-1,s,e)
        if s<pivot: answer=max(answer, getAnswer(s, pivot-1))
        if pivot<e: answer=max(answer, getAnswer(pivot+1,e))
    return answer
                                
                                   

n=int(input())
minTree=[0]*(4*n)
sumTree=[0]*(4*n)
number=tuple(map(int,input().split()))

makeSumSeg(1,0,n-1)
makeMinSeg(1,0,n-1)

print(getAnswer(0,n-1))
