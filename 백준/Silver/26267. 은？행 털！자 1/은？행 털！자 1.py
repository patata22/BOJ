import sys
input=sys.stdin.readline

record={}
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if a-b not in record:record[a-b]=0
    record[a-b]+=c
print(max([record[x] for x in record]))

