def solution(num_list, n):
    N= len(num_list)//n
    answer = [[] for i in range(N)]
    for i in range(0,len(num_list),n):
        for j in range(i,i+n):
            answer[i//n].append(num_list[j])
    return answer