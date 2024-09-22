for _ in range(int(input())):
    answer=0
    word=list(input())
    n=len(word)
    for i in range(n-2):
        if word[i]==word[i+2]=='W' and word[i+1]=='O':answer+=1
    print(answer)
