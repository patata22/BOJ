import sys
input=sys.stdin.readline

def makeSeg(node,s,e):
    if s==e:
        tree[node]=number[s]
    else:
        mid=(s+e)//2
        tree[node]=makeSeg(node*2, s,mid)+makeSeg(node*2+1,mid+1,e)
    return tree[node]

def update(node, s,e,idx,diff):
    if not s<=idx<=e: return
    tree[node]+=diff
    if s!=e:
        mid=(s+e)//2
        update(node*2, s, mid, idx, diff)
        update(node*2+1, mid+1, e, idx, diff)

def getSum(node, s,e,l,r):
    if l>e or r<s: return 0
    elif l<=s and e<=r: return tree[node]
    else:
        mid=(s+e)//2
        return getSum(node*2, s, mid, l, r)+getSum(node*2+1, mid+1,e, l, r)


n,m,k=map(int,input().split())
number=[0]+[int(input()) for i in range(n)]
tree=[0]*4000000


makeSeg(1,0,n)
for _ in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        diff=c-number[b]
        number[b]=c
        update(1,0,n,b,diff)
    elif a==2:
        print(getSum(1,0,n,b,c))
