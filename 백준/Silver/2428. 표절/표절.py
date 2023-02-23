n=int(input())
file = list(map(int,input().split()))
file.sort()
answer=0
l=0
r=0
while r<n-1:
    r+=1
    while file[l]<0.9*file[r]:
        l+=1
    answer+=r-l
print(answer)
