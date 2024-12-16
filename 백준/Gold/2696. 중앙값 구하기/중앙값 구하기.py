import sys,heapq
input=sys.stdin.readline

for tt in range(int(input())):
    m=int(input())
    n=m//10
    left=[]    
    right=[]
    answer=[]
    if m%10: n+=1
    for _ in range(n):
        temp=list(map(int,input().split()))
        for j in range(len(temp)):
            x=temp[j]
            if not left:
                left.append(-x)
                answer.append(x)
            else:
                middle=-left[0]
                if x>=middle: heapq.heappush(right,x)
                else: heapq.heappush(left,-x)
                while len(left)>len(right)+1:
                    heapq.heappush(right,-heapq.heappop(left))
                while len(left)<len(right)+1:
                    heapq.heappush(left,-heapq.heappop(right))
                if j%2==0:
                    answer.append(-left[0])
        
    print(len(answer))
    for i in range(len(answer)):
        x=answer[i]
        if i%10!=9:print(x,end=' ')
        else: print(x)
    if i!=9: print()