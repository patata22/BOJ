S=input()
A=input()
B=input()

n=len(S)
a=len(A)
b=len(B)
answer=set()

left=[]
for i in range(n-a+1):
    if S[i:i+a]==A:left.append(i)

right=[]
for i in range(b-1,n):
    if S[i-b+1:i+1]==B:right.append(i)

for i in left:
    for j in right:
        if j>=i+a-1 and j-b+1>=i: answer.add(S[i:j+1])

print(len(answer))