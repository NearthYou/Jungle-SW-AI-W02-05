# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

# 가장 적은 종류 -> 최단 거리
# 다른 국가를 거쳐가도 됨(이미 방문했어도 됨)

# 테스트 케이스 <= 100
# 국가 수 N, 비행기 종류 M
# a -> b 비행 스케줄

# from collections import deque

# def bfs(graph, start):
#     visited = [False] * len(graph)

#     q = deque()
#     q.append(start)
#     visited[start] = True

#     result = []
#     while q:
#         cur = q.popleft()
#         result.append(cur)
        
#         for v in graph[cur]:
#             if not visited[v]:
#                 visited[v] = True
#                 q.append(v)
#     return result

# n = int(input())

# result = []
# for _ in range(n):
#     c, f = map(int, input().split())
#     graph = [[] for _ in range(c + 1)]
#     for i in range(f):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)
    
#     rs = bfs(graph, 1)
#     result.append(len(rs) - 1)

# for i in result:
#     print(i)

from collections import deque

n = int(input())

result = []
for _ in range(n):
    c, f = map(int, input().split())
    graph = [[] for _ in range(c + 1)]
    for i in range(f):
        u, v = map(int, input().split())
    
    result.append(c - 1)

for i in result:
    print(i)