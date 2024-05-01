def sol():
    change=True
    answer=0
    while change:
        cnt=0
        for i in range(n):
            if not number[i]:cnt+=1
        if cnt==n: return answer
        change=False
        double=True
        for i in range(n):
            if number[i]%2==1:
                double=False
        if double:
            for i in range(n):
                number[i]//=2
            change=True
            answer+=1
            continue
        else:
            for i in range(n):
                if number[i]%2==1:
                    change=True
                    number[i]-=1
                    answer+=1
    
n=int(input())
number=list(map(int,input().split()))
print(sol())