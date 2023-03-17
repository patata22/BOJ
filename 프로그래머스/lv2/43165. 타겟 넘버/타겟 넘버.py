def solution(numbers, target):
    global answer
    answer = 0
    dfs(0,0,len(numbers), target, numbers)
    
    return answer

def dfs(count, now,n, target,numbers):
    global answer
    if count==n:
        if now==target:
            answer+=1
        return
    dfs(count+1, now+numbers[count], n, target,numbers)
    dfs(count+1, now-numbers[count], n, target,numbers)
    
            