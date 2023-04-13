import sys
input=sys.stdin.readline

def makeSeg(node,s,e):
    if s==e:
        tree[node]=number[s]
    else:
        mid=(s+e)//2
        makeSeg(node*2,s,mid)
        makeSeg(node*2+1,mid+1,e)

def propagate(node,s,e):
    if s!=e:
        lazy[node*2]+=lazy[node]
        lazy[node*2+1]+=lazy[node]
    else:
        tree[node]+=lazy[node]
    lazy[node]=0
    return

        
def update(node,s,e,l,r,value):
    propagate(node,s,e)
    if e<l or s>r: return
    elif l<=s and e<=r:
        lazy[node]+=value
        propagate(node,s,e)
    else:
        mid=(s+e)//2
        update(node*2,s,mid,l,r,value)
        update(node*2+1,mid+1,e,l,r,value)
        
def getAnswer(node,s,e,idx):
    propagate(node,s,e)
    if not s<=idx<=e: return 0
    if s==e==idx:
        return tree[node]
    else:
        mid=(s+e)//2
        return getAnswer(node*2,s,mid,idx)+getAnswer(node*2+1,mid+1,e,idx)

n=int(input())
number=[0]+list(map(int,input().split()))

tree=[0]*(4*n)
lazy=[0]*(4*n)
makeSeg(1,1,n)

for _ in range(int(input())):
    temp=list(map(int,input().split()))
    if temp[0]==1:
        update(1,1,n,temp[1],temp[2],temp[3])
    else:
        print(getAnswer(1,1,n,temp[1]))
