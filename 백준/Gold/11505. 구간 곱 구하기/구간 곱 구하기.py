import sys
input=sys.stdin.readline
DIV=1000000007

def makeSeg(node,s,e):
    if s==e:
        tree[node]=number[s]
    else:
        mid=(s+e)//2
        tree[node]=((makeSeg(node*2, s, mid)%DIV)*(makeSeg(node*2+1,mid+1,e)%DIV))%DIV
    return tree[node]

def update(node,s,e,idx,value):
    if not s<=idx<=e: return 
    elif s==e:
        tree[node]=value
    else:
        mid=(s+e)//2
        update(node*2, s, mid, idx, value)
        update(node*2+1,mid+1,e,idx,value)
        tree[node]= ((tree[node*2]%DIV)*(tree[node*2+1]%DIV))%DIV
    return tree[node]

def getMul(node,s,e,l,r):
    if e<l or s>r: return 1
    elif l<=s and e<=r: return tree[node]
    else:
        mid=(s+e)//2
        return ((getMul(node*2, s, mid, l, r)%DIV)*(getMul(node*2+1, mid+1, e, l, r)%DIV))%DIV
        
n,m,k=map(int,input().split())
number=[0]+[int(input()) for i in range(n)]
tree=[1]*4000000

makeSeg(1,1,n)

for _ in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        update(1,1,n,b,c)
    else:
        print(getMul(1,1,n,b,c))
