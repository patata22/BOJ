def solution(p):
    if not p: return p
    balanced=True
    left,right=0,0
    stack=[]
    idx=0
    while not left or left!=right:
        if p[idx]=='(':
            left+=1
            stack.append('(')
        else:
            if not stack or stack[-1]!='(':
                balanced=False
            right+=1
        idx+=1
    U= p[:idx]
    V= p[idx:]
    if balanced:
        return U + solution(V)
    else:
        return '(' + solution(V) + ')' + reverse(p[1:idx-1])
    
def reverse(S):
    temp=""
    for s in S:
        if s=='(': temp+=')'
        else: temp+='('
    return temp