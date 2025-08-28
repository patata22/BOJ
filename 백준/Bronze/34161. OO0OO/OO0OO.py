input()
input()
input()

for a in range(1,11):
    for b in range(1,11):
        for c in range(1,11):
            for d in range(1,11):
                result=1000*a+b-1000*d                
                if result<0: print(-1)
                else: print(result)