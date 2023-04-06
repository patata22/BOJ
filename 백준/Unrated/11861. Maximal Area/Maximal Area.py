import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def makeSeg(node,s,e):
    if s==e:
        tree[node]=s
    else:
        mid=(s+e)//2
        a=makeSeg(node*2,s,mid)
        b=makeSeg(node*2+1,mid+1,e)
        if number[a]<number[b]: tree[node]=tree[node*2]
        else: tree[node]=tree[node*2+1]
    return tree[node]

def getMin(node,s,e,l,r):
    if e<l or s>r: return -1
    elif l<=s and e<=r: return tree[node]
    else:
        mid=(s+e)//2
        a=getMin(node*2,s,mid,l,r)
        b=getMin(node*2+1,mid+1,e,l,r)
        if a==-1: return b
        elif b==-1: return a
        elif number[a]<number[b]: return a
        else: return b

def getAnswer(s,e):
    if s==e: return number[s]
    pivot = getMin(1,0,n-1,s,e)
    answer=number[pivot]*(e-s+1)
    if s<pivot:
        answer=max(answer, getAnswer(s,pivot-1))
    if pivot<e:
        answer=max(answer, getAnswer(pivot+1,e))

    return answer

n=int(input())
number=tuple(map(int,input().split()))
tree=[0]*(4*n)

makeSeg(1,0,n-1)

print(getAnswer(0,n-1))
