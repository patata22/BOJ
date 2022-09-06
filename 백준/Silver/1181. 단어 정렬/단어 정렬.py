word=[input() for i in range(int(input()))]
word.sort(key=lambda x: (len(x),x))
visited=set()
for x in word:
    if x not in visited:
        visited.add(x)
        print(x)
