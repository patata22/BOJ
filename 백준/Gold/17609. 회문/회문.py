def check(l,r):
    while l<r:
        if word[l]!=word[r]: return False
        l+=1
        r-=1
    return True
    
def sol():
    n=len(word)
    l=0
    r=n-1
    while l<r:
        if word[l]!=word[r]:
            if check(l+1,r) or check(l,r-1): return 1
            else: return 2
        l+=1
        r-=1
    return 0

for _ in range(int(input())):
    word=list(input())
    print(sol())