import sys
input=sys.stdin.readline

m,n=map(int,input().split())
key=[]
for _ in range(n):
    a,b,c=input().split()
    a,b=int(a),int(b)
    key.append((a,b,c))
key.sort(key=lambda x: (x[1],x[0]))

answer=[]
for a,b,c in key:
    answer.append(c)
print(''.join(answer))