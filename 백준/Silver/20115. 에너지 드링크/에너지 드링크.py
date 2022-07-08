import heapq

n=int(input())
drink=list(map(int,input().split()))
drink.sort()
print(drink[-1]+0.5*sum(drink[:n-1]))