import sys
input=sys.stdin.readline

n=int(input())
dic={}
for _ in range(n):
    temp = input().rstrip()
    if len(temp)==1: continue
    a,b,c=temp[0],temp[-1],''.join(sorted(temp[1:len(temp)-1]))
    dic[a+b+c]=temp
    
    
input()
for x in input().rstrip().split():
    if len(x)==1: print(x, end=' ')
    else:
        a,b,c=x[0],x[-1],''.join(sorted(x[1:len(x)-1]))
        print(dic[a+b+c],end=' ')
        
