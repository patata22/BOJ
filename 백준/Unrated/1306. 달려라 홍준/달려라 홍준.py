import sys
input=sys.stdin.readline

def makeSeg(node,s,e):
    if s==e:
        tree[node]=number[s]
    else:
        mid=(s+e)//2
        tree[node]= max(makeSeg(node*2, s, mid),makeSeg(node*2+1, mid+1, e))
    return tree[node]

def getMax(node,s,e,l,r):
    if e<l or s>r: return 0
    elif l<=s and e<=r: return tree[node]
    else:
        mid=(s+e)//2
        return max(getMax(node*2,s,mid,l,r), getMax(node*2+1,mid+1,e,l,r))
    

n,m=map(int,input().split())
number=[0]+list(map(int,input().split()))
tree=[0]*4000000
makeSeg(1,0,n)
answer=[]
for i in range(m,n-m+2):
    answer.append(getMax(1,0,n,i-m+1,i+m-1))
print(*answer)
    
