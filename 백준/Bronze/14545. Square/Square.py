import sys
input=sys.stdin.readline

answer=[0]*1000001
for i in range(1,1000001):
    answer[i]=answer[i-1]+i**2

for _ in range(int(input())):
    print(answer[int(input())])
    