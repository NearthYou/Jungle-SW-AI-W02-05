# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

from collections import deque

n = int(input())
m = int(input())

graph = [[] for i in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph, start):

    visited = [False] * (n + 1)

    q = deque([start])
    visited[start] = True

    result = []
    while q:
        cur = q.popleft()
        result.append(cur)

        for next in graph[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
    return result

print(len(bfs(graph, 1)) - 1)
# 1번부터 시작 BFS result의 길이 변환