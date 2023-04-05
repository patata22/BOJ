import sys
input=sys.stdin.readline

def makeMaxSeg(node,s,e):
    if s==e:
        maxTree[node]=number[s]
    else:
        mid=(s+e)//2
        maxTree[node]= max(makeMaxSeg(node*2,s,mid), makeMaxSeg(node*2+1,mid+1,e))
    return maxTree[node]

def makeMinSeg(node,s,e):
    if s==e:
        minTree[node]=number[s]
    else:
        mid=(s+e)//2
        minTree[node]=min(makeMinSeg(node*2,s,mid),makeMinSeg(node*2+1,mid+1,e))
    return minTree[node]

def getMax(node,s,e,l,r):
    if e<l or s>r: return 0
    elif l<=s and e<=r: return maxTree[node]
    else:
        mid=(s+e)//2
        return max(getMax(node*2, s,mid, l,r), getMax(node*2+1, mid+1,e,l,r))
def getMin(node,s,e,l,r):
    if e<l or s>r: return float('inf')
    elif l<=s and e<=r: return minTree[node]
    else:
        mid=(s+e)//2
        return min(getMin(node*2, s, mid, l, r),getMin(node*2+1,mid+1,e,l,r))
    


n,m=map(int,input().split())
number=[0]+[int(input()) for i in range(n)]
maxTree=[0]*400000
minTree=[0]*400000
makeMaxSeg(1,1,n)
makeMinSeg(1,1,n)

for _ in range(m):
    a,b=map(int,input().split())
    print(getMin(1,1,n,a,b), getMax(1,1,n,a,b))
