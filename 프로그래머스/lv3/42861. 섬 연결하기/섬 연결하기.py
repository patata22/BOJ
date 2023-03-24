def solution(n, costs):
    parent=[-1]*n
    def find(a):
        if parent[a]<0: return a
        else:
            parent[a]=find(parent[a])
            return parent[a]
    def union(a,b):
        pa=find(a)
        pb=find(b)
        if pa!=pb: parent[b]=pa
        
    answer=0
    count=0
    costs.sort(key= lambda x: x[2])
    for i in range(len(costs)):
        start, end, cost = costs[i]
        a,b= find(start), find(end)
        if a!=b:
            answer+=cost
            union(a,b)
            count+=1
            if count==n-1: return answer
    