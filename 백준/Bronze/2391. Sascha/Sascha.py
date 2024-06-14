for tt in range(int(input())):
    target=input()
    answer=''
    count=float('inf')
    words=[input() for i in range(int(input()))]
    for word in words:
        cnt=0
        for i in range(len(target)):
            if target[i]!=word[i]: cnt+=1
        if cnt<count:
            count=cnt
            answer=word
    print(answer)
