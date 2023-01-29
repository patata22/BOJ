for t in range(1,int(input())+1):
    if t!=1: print()
    print(f'Scenario #{t}:')
    n=int(input())
    word = [input() for i in range(n)]
    for _ in range(int(input())):
        answer=""
        count=list(map(int,input().split()))[1:]

        for x in count:
            answer+=word[x]
            
        print(answer)
    
