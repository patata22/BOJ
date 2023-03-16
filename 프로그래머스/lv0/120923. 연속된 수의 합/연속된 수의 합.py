def solution(n, total):
    x= (2*total - (n*(n-1)))//(2*n)
    return [i for i in range(x, x+n)]