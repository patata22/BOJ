import sys
input=sys.stdin.readline
for _ in range(int(input())):
    answer=0
    n=int(input())
    media=set(input().rstrip())
    for __ in range(n):
        temp=input().rstrip()
        for x in media:
            if x in temp:
                answer+=1
                break
            
    print(f'Data Set {_+1}:\n{answer}\n')
    