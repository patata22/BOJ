import sys
input=sys.stdin.readline

def update(node,s,e,idx,value):
    if not s<=idx<=e: return
    elif s==e: tree[node]+=value
    else:
        mid=(s+e)//2
        update(node*2, s,mid, idx, value)
        update(node*2+1,mid+1,e,idx,value)
        tree[node]=tree[node*2]+tree[node*2+1]
    return tree[node]

def getSum(node,s,e,l,r):
    if e<l or s>r: return 0
    elif l<=s and e<=r: return tree[node]
    else:
        mid=(s+e)//2
        return getSum(node*2,s,mid, l,r)+getSum(node*2+1,mid+1,e,l,r)


n,q=map(int,input().split())
tree=[0]*(4*n)
for _ in range(q):
    a,b,c=map(int,input().split())
    if a==1:
        update(1,1,n,b,c)
    else:
        print(getSum(1,1,n,b,c))
