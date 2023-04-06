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

def getSum(node, s,e,l,r):
    if s>r or e<l: return 0
    elif l<=s and e<=r: return tree[node]
    else:
        mid=(s+e)//2
        return getSum(node*2,s,mid,l,r)+getSum(node*2+1,mid+1,e,l,r)

def sol(s,e,num):
    if s==e:return e
    sumNow= getSum(1,0,n,s,e)
    if sumNow==num:return e
    else:
        mid=(s+e)//2
        temp=getSum(1,0,n,s,mid)
        if temp>=num:
            return sol(s,mid,num)
        else:
            return sol(mid+1,e,num-temp)

n=int(input())
number=[0]+list(map(int,input().split()))
tree=[0]*(4*n)

makeSeg(1,0,n)

for _ in range(int(input())):
    temp=list(map(int,input().split()))
    if temp[0]==1:
        update(1,0,n,temp[1],temp[2])
    else:
        print(sol(0,n,temp[1]))
