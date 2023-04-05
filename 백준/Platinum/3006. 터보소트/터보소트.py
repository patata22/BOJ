import sys
input=sys.stdin.readline

def makeSeg(node,s,e):
    if s!=e:
        mid=(s+e)//2
        tree[node]=makeSeg(node*2,s,mid)+makeSeg(node*2+1,mid+1,e)
    return tree[node]

def getSum(node,s,e,l,r):
    if e<l or s>r: return 0
    elif l<=s and e<=r: return tree[node]
    else:
        mid=(s+e)//2
        return getSum(node*2, s, mid, l, r)+ getSum(node*2+1, mid+1, e, l, r)

def update(node,s,e,idx):
    if not s<=idx<=e: return
    elif s==e: tree[node]=0
    else:
        mid=(s+e)//2
        update(node*2, s,mid,idx)
        update(node*2+1, mid+1,e,idx)
        tree[node]=tree[node*2]+tree[node*2+1]
    return tree[node]

n=int(input())
location={}
for i in range(1,n+1):
    location[int(input())]=i

tree=[1]*(4*n)
makeSeg(1,1,n)
l=1
r=n

for i in range(n):
    if not i%2:
        print(getSum(1,1,n,1,location[l]-1))
        update(1,1,n,location[l])
        l+=1
    else:
        print(getSum(1,1,n,location[r]+1,n))
        update(1,1,n,location[r])
        r-=1