def solution(data, col, row_begin, row_end):
    
    answer = 0
    data= sorted(data, key= lambda x: (x[col-1], -x[0]))
    for i in range(row_begin, row_end+1):
        answer^=getS(data[i-1], i)
    return answer

def getS(row, i):
    return sum(map(lambda x: x%i, row))