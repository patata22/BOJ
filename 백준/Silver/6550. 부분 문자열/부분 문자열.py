while True:
    try:
        a,b=input().split()
        l=0
        r=0
        while l<len(a) and r<len(b):
            if a[l]==b[r]:l+=1
            r+=1
        print('Yes') if l==len(a) else print('No')
    except EOFError:break
