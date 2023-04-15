l,r=2,2
n=int(input())
while l*r<n:
    if l>r: r+=1
    else: l+=1
print(2*(l+r-2))