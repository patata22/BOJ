def solution(ineq, eq, n, m):
    s=str(n)+ineq
    if eq=='=': s+=eq
    s+=str(m)
    return int(eval(s))