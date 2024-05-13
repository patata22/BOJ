def sol():
    for _ in range(int(input())):
        name=list(input())
        big=0
        small=0
        alpha=0
        for x in name:
            if x.isalpha():
                if x.isupper():big+=1
                else: small+=1
            if not x.isnumeric():alpha=1
        if big<=small and alpha and len(name)<=10:
            return ''.join(name)
print(sol())
        
