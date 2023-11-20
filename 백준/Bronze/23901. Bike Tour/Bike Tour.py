for t in range(1,int(input())+1):
    n=int(input())
    height=tuple(map(int,input().split()))
    answer=0
    for i in range(1,n-1):
        if height[i]>height[i-1] and height[i]>height[i+1]:answer+=1
    print(f'Case #{t}: {answer}')

    