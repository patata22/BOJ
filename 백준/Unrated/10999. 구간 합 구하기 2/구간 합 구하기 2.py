import sys
input=sys.stdin.readline

def makeSeg(node,s,e):
    if s==e:
        tree[node]=number[s]
    else:
        mid=(s+e)//2
        tree[node]=makeSeg(node*2,s,mid)+makeSeg(node*2+1,mid+1,e)
    return tree[node]

def propagate(node, s, e):
    if s!=e:
        lazy[node*2]+=lazy[node]
        lazy[node*2+1]+=lazy[node]
    tree[node]+=lazy[node]*(e-s+1)
    lazy[node]=0
    return

def update(node,s,e,l,r,value):
    if s==e and s==l:
        if lazy[node]:
            tree[node]+=lazy[node]
            lazy[node]=0
        tree[node]+=value
        return tree[node]
    else:
        if lazy[node]:
            propagate(node,s,e)

        if l<=s and e<=r:
            tree[node]+=value*(e-s+1)
            if s!=e:
                lazy[node*2]+=value
                lazy[node*2+1]+=value
            return tree[node]
        elif e<l or r<s:
            return tree[node]
        else:
            mid=(s+e)//2
            a= update(node*2, s,mid,l,r,value)
            b= update(node*2+1, mid+1,e,l,r, value)
            tree[node]=a+b
            return tree[node]

def query(node,s,e,l,r):
    if s==e and s==l:
        if lazy[node]:
            tree[node]+=lazy[node]
            lazy[node]=0
        return tree[node]
    else:
        if lazy[node]:   
            propagate(node,s,e)
        if l<=s and e<=r: return tree[node]
        elif s>r or e<l: return 0
        else:
            mid=(s+e)//2
            a=query(node*2,s,mid,l,r)
            b=query(node*2+1,mid+1,e,l,r)
            tree[node]=tree[node*2]+tree[node*2+1]
            return a+b


    
n,m,k=map(int,input().split())

number=[0]
for _ in range(n): number.append(int(input()))

tree=[0]*(4*n)
lazy=[0]*(4*n)
makeSeg(1,1,n)

for _ in range(m+k):
    temp=tuple(map(int,input().split()))
    if temp[0]==1:
        update(1,1,n,temp[1],temp[2],temp[3])
    else:
        print(query(1,1,n,temp[1],temp[2]))
