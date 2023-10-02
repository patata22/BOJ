nxt={'w':'o','o':'l','l':'f','f':'w'}

answer=1
word=list(input())
now='f'
countBefore=0
countNow=0

for x in word:
    if x==now: countNow+=1
    else:
        if x==nxt[now]:
            if now=='f':
                if countNow and countBefore!=countNow:
                    answer=0
                    break
                countNow=1
                now=x
            elif now=='w':
                countBefore=countNow
                countNow=1
                now=x
            else:
                if countBefore!=countNow:
                    answer=0
                    break
                countBefore=countNow
                countNow=1
                now=x
        else:
            answer=0
            break
if now!='f': answer=0
if countBefore!=countNow:answer=0
print(answer)
        
