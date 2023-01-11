import sys
input=sys.stdin.readline


answer=0
record=set()
for _ in range(int(input())):
    a,b= map(int,input().split())
    if b:
        if a not in record: record.add(a)
        else:answer+=1
    else:
        if a not in record:answer+=1
        else: record.remove(a)

print(answer+len(record))
