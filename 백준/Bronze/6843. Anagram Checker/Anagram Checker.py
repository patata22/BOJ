a=input()
b=input()
answer='Is an anagram.'
for x in a:
    if x==' ': continue
    if a.count(x)!=b.count(x): answer='Is not an anagram.'

print(answer)
