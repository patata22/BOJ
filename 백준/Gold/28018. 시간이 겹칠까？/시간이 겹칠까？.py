import sys
input=sys.stdin.readline

number=[0]*1000002
number[0]=0
for _ in range(int(input())):
    s,e=map(int,input().split())
    number[s]+=1
    number[e+1]-=1

for i in range(1,1000001):
    number[i]+=number[i-1]
input()
for x in map(int,input().split()):
    print(number[x])