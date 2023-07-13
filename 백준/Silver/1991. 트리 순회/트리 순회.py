def preorder(x):
    print(x,end='')
    b,c=graph[x]
    if b!='.':preorder(b)
    if c!='.':preorder(c)

def order(x):
    b,c=graph[x]
    if b!='.':order(b)
    print(x,end='')
    if c!='.':order(c)

def postorder(x):
    b,c=graph[x]
    if b!='.':postorder(b)
    if c!='.':postorder(c)
    print(x,end='')
n=int(input())
graph={}
for _ in range(n):
    a, b, c = input().split()
    graph[a]= []
    graph[a].append(b)
    graph[a].append(c)

preorder('A')
print()
order('A')
print()
postorder('A')
