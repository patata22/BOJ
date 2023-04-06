import sys
input=sys.stdin.readline

def makeSeg(node,s,e):
    if s==e:
        tree[node]=number[s]
    else:
        mid=(s+e)//2
        tree[node]=makeSeg(node*2,s,mid)+makeSeg(node*2+1,mid+1,e)
    return tree[node]

def update(node, s,e,idx, difference):
    if not s<=idx<=e: return
    elif s==e: tree[node]+=difference
    else:
        mid=(s+e)//2
        update(node*2,s,mid,idx,difference)
        update(node*2+1,mid+1,e,idx,difference)
        tree[node]=tree[node*2]+tree[node*2+1]

def sol(node,s,e,num):
    if s==e:return e
    mid=(s+e)//2
    if tree[node*2]>=num: return sol(node*2,s,mid,num)
    else: return sol(node*2+1,mid+1,e,num-tree[node*2])

n=int(input())
number=[0]+list(map(int,input().split()))
tree=[0]*(4*n)

makeSeg(1,0,n)

for _ in range(int(input())):
    temp=list(map(int,input().split()))
    if temp[0]==1:
        update(1,0,n,temp[1],temp[2])
    else:
        print(sol(1,0,n,temp[1]))
