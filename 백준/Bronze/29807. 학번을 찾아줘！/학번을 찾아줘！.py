t=int(input())
score=list(map(int,input().split()))
while len(score)<5: score.append(0)

a,b,c,d,e=score

if a>c: A= (a-c)*508
else: A=  (c-a)*108
if b>d: B = (b-d)*212
else: B = (d-b)*305
C = e*707

print((A+B+C)*4763) 
