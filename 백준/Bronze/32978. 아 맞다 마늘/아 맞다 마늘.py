input()
recipe=set(input().split())
for x in input().split():
    recipe.remove(x)
for x in recipe:print(x)
