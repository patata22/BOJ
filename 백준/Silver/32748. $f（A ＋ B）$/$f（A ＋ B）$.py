change=list(map(int,input().split()))
a,b=map(int,input().split())
temp=[]
while a:
    temp.append(change.index(a%10))
    a//=10
a=int(''.join(map(str,temp[::-1])))
temp=[]
while b:
    temp.append(change.index(b%10))
    b//=10
a+=int(''.join(map(str,temp[::-1])))
answer=[]
while a:
    answer.append(change[a%10])
    a//=10
print(''.join(map(str,answer[::-1])))