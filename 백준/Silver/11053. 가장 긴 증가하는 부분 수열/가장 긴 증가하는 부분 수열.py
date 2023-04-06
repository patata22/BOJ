import sys
input=sys.stdin.readline

def update(node,s,e,idx,value):
    if not s<=idx<=e: return
    elif s==e:
        tree[node]=value
    else:
        mid=(s+e)//2
        update(node*2,s,mid,idx,value)
        update(node*2+1,mid+1,e,idx,value)
        tree[node]=max(tree[node*2],tree[node*2+1])

def getMax(node,s,e,l,r):
    if e<l or s>r: return 0
    elif l<=s and e<=r: return tree[node]
    else:
        mid=(s+e)//2
        return max(getMax(node*2, s,mid,l,r),getMax(node*2+1,mid+1,e,l,r))

n=int(input())
tree=[0]*(4*n)
number=list(map(int,input().split()))
number=sorted(enumerate(number), key=lambda x: (x[0],-x[1]))
number.sort(key=lambda x: (x[1],-x[0]))
for i,x in number:
    update(1,0,n-1,i,getMax(1,0,n-1,0,i)+1)
print(tree[1])
