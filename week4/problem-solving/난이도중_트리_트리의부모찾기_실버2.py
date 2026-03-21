# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725



# parent = [0 for _ in range(n + 1)]
# root = 1

# for i in range(n - 1):
#     u, v = map(int, input().split())
#     if (parent[v] and not parent[u]) or v is root:
#         parent[u] = v
#     else:
#         parent[v] = u

# for i in range(2, len(parent)):
#     print(parent[i])

from collections import deque
n = int(input())

def bfs(graph, start):

    parent = [0 for _ in range(n + 1)]

    q = deque([start])
    parent[1] = 1

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if parent[next] == 0:
                parent[next] = cur
                q.append(next)
    return parent
               
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = bfs(graph, 1)
for i in range(2, len(result)):
    print(result[i])