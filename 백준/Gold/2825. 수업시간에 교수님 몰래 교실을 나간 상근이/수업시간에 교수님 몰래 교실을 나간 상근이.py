import sys
input=sys.stdin.readline

def change(x):
    result=0
    while x:
        result|=(1<<(x%10))
        x//=10
    return result

n=int(input())
number=[int(input()) for i in range(n)]

count=[0]*1024

for x in number:
    count[change(x)]+=1

answer=0

for i in range(1024):
    cnt=count[i]
    answer+=(cnt*(cnt-1))//2
    for j in range(i+1,1024):
        if i&j: answer+=cnt*count[j]
print(answer)