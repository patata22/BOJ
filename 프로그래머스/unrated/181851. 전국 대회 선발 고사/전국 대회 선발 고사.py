def solution(rank, attendance):
    answer = []
    rank=sorted(enumerate(rank),key=lambda x: x[1])
    cnt=3
    for i,x in rank:
        if attendance[i]:
            answer.append(i)
            cnt-=1
            if not cnt: break
    a,b,c=answer
    return 10000*a+100*b+c