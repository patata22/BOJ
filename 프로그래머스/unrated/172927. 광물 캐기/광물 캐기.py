def solution(picks, minerals):
    mineral = {"stone": 2, "iron":1, "diamond": 0}
    tire=[(1,1,1), (5,1,1,), (25,5,1)]
    
    answer = float('inf')
    minerals = list(map(lambda x: mineral[x], minerals))
    minerals=minerals[::-1]
    
    def dfs(tire_now):
        nonlocal answer
        for pick in range(3):
            if picks[pick]:
                temp_tire=0
                picks[pick]-=1
                temp=[]
                for i in range(min(5,len(minerals))):
                    target=minerals.pop()
                    temp_tire+=tire[pick][target]
                    temp.append(target)
                if not minerals or sum(picks)==0:
                    answer=min(tire_now+temp_tire,answer)
                else:
                    dfs(tire_now+temp_tire)
                picks[pick]+=1
                while temp: minerals.append(temp.pop())
                
    dfs(0)
    
    return answer