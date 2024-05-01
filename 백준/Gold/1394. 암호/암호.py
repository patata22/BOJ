DIV = 900528

def sol():
    answer=0
    for x in target:
        answer*=n
        answer+=record[x]
        answer%=DIV
    return answer
    

record={}
word=list(input())
n=len(word)
for i in range(n):
    record[word[i]]=i+1
target=list(input())
print(sol())
