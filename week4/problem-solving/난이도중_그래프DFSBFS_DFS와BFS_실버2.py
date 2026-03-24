# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

import sys
from collections import deque
input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start):
    visited = [False] * len(graph)
    visited[start] = True
    q = deque([start])

    result = []
    while q:
        cur = q.popleft()
        result.append(cur)

        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
    return result

def dfs(graph, start, visited = None):
    
    if visited is None:
        visited = []

    visited.append(start)

    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    
    return visited

print(dfs(graph, x))
print(bfs(graph, x))