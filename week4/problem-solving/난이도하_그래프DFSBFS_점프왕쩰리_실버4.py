# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

# 정사각형의 보드가 주어진다.
# 항상 0,0 에서 시작
# 이동 가능한 방향은 오른쪽과 아래 뿐
# 맨 오른쪽 하단 칸에 도달하는 순간 젤리 승리
# 현재 밟고 있는 칸에 쓰여 있는 수 만큼 이동.
# 대신 딱 그 수만큼 이동할 수 있어야함 초과나 미만 금지

from collections import deque

dr = [1, 0]
dc = [0, 1]

def bfs(graph):
    n = len(graph)
    visited = [[False] * n for _ in range(n)]

    q = deque()
    q.append((0, 0))
    visited[0][0] = graph[0][0]

    while q:
        r, c = q.popleft()
        jump = graph[r][c]

        if jump == -1:
            return "HaruHaru"
        
        for i in range(2):
            nr = r + dr[i] * jump
            nc = c + dc[i] * jump

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc)) 
        
    return "Hing"

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

print(bfs(board))