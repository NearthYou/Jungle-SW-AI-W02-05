# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

from collections import deque
import sys
input = sys.stdin.readline

def solve():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    n, m = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(n)]
    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 1:
                board[nr][nc] = board[r][c] + 1
                q.append((nr, nc))

    print(board[n - 1][m - 1])

solve()