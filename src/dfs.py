# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v,end=' ')
#     for it in graph[v]:
#         if not visited[it]:
#             dfs(graph, it, visited)

# graph=[
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7 ]
# ]
# visited = [False] * 9
# dfs(graph, 1, visited)


#ex ) 
# 영역 나누기
n, m = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x <=- 1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x -1, y)
        dfs(x, y -1)
        dfs(x +1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)







