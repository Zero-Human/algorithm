total = int(input())
person = []
for it in range(total):
    person.append(list(map(int,input().split()))+[it])

result = [0]*len(person)

for idx,it in enumerate(person):
    count = 1
    for it2 in person:
        if it[0] < it2[0] and it[1] < it2[1]:
            count+=1
    result[it[2]] = count 

for it in result:
    print(it, end =' ')
# 완전 탐색하여 각각의 순위를 찾는 방식으로함