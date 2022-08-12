for _ in range(int(input())):
    count={}
    for i in range(65,91):
        count[chr(i)]=0
    answer="OK"
    text=input()
    idx=0
    while idx<len(text):
        count[text[idx]]+=1
        if count[text[idx]]%3==0:
            try:
                if text[idx+1]!=text[idx]:
                    answer="FAKE"
                    break
            except IndexError:
                answer="FAKE"
                break
            idx+=1
        idx+=1

    print(answer)
