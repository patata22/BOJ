def solution(enroll, referral, seller, amount):
    n=len(enroll)
    answer = [0]*(n+1)
    
    numbering={"-":0}
    for i, name in enumerate(enroll):
        numbering[name]=i+1
        
    refer={}
    for i, name in enumerate(referral):
        refer[i+1]=numbering[name]
    
    def distribute(now, money):
        nxt_money= money//10
        answer[now]+= money - nxt_money
        nxt_member = refer[now]
        if nxt_member and nxt_money: distribute(nxt_member, nxt_money)
    
    for i in range(len(seller)):
        member=numbering[seller[i]]
        money = amount[i]*100
        distribute(member, money)
    return answer[1:]