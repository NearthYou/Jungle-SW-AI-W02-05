# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707

import sys
from collections import deque

input = sys.stdin.readline

def solve():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [0] * (v + 1)

    for i in range(1, v + 1):
        if visited[i] == 0:
            q = deque([i])
            visited[i] = 1
            
            while q:
                cur = q.popleft()
                for next_node in graph[cur]:
                    if visited[next_node] == 0:
                        visited[next_node] = 3 - visited[cur]
                        q.append(next_node)
                    elif visited[next_node] == visited[cur]:
                        print("NO")
                        return

    print("YES")

k = int(input())
for _ in range(k):
    solve()