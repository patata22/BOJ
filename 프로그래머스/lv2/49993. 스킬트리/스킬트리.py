def solution(skill, skill_trees):
    answer = 0
    order= {}
    for i in range(len(skill)):
        order[skill[i]]=i
    
    for trees in skill_trees:
        flag=True
        now=0
        for tree in trees:
            if tree in order and now<order[tree]:
                flag=False
                break
            elif tree in order and now==order[tree]:
                now+=1
        answer+=flag
   
    return answer