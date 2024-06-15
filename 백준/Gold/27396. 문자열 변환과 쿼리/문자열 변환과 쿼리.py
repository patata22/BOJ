import sys
input=sys.stdin.readline

s,n=input().split()
s=list(map(ord,s))
n=int(n)
change=[i for i in range(125)]

for _ in range(n):
    temp=input().split()
    if temp[0]=='2':
        temp=[]
        for x in s: temp.append(chr(change[x]))
        print(''.join(temp))
        
    else:
        b,c=ord(temp[1]),ord(temp[2])
        for i in range(65,125):
            if change[i]==b:
                
                change[i]=c
                