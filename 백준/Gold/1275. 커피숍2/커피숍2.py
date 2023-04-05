import sys
input=sys.stdin.readline

def makeSeg(node,s,e):
    if s==e:tree[node]=number[s]
    else:
        mid=(s+e)//2
        tree[node]=makeSeg(node*2, s, mid)+makeSeg(node*2+1, mid+1, e)
    return tree[node]

def update(node,s,e,idx,number):
    if not s<=idx<=e: return
    elif s==e:
        tree[node]=number
    else:
        mid=(s+e)//2
        update(node*2, s,mid,idx,number)
        update(node*2+1, mid+1,e,idx,number)
        tree[node]=tree[node*2]+tree[node*2+1]

def getSum(node,s,e,l,r):
    if e<l or s>r: return 0
    elif l<=s and e<=r: return tree[node]
    else:
        mid=(s+e)//2
        return getSum(node*2,s,mid,l,r)+getSum(node*2+1, mid+1,e,l,r)

n,q=map(int,input().split())
number=[0]+list(map(int,input().split()))
tree=[0]*(4*n)

makeSeg(1,1,n)

for _ in range(q):
    a,b,c,d=map(int,input().split())
    if a>b: a,b=b,a
    print(getSum(1,1,n,a,b))
    update(1,1,n,c,d)

    