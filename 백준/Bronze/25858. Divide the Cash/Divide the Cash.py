n,d=map(int,input().split())
count=[int(input()) for i in range(n)]
total= sum(count)
for x in count:
    print(d*x//total)
