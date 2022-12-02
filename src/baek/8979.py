country_count, target = map(int,input().split())
country_map = [list(map(int,input().split())) for _ in range(country_count)]
result = sorted(country_map,key = lambda item: (item[1],item[2],item[3]),reverse= True )
cmp = []
for it in result:
    if it[0] == target:
        cmp = it
for idx,it in enumerate(result):
    if it[1:] == cmp[1:]:
        print(idx+1)
        break