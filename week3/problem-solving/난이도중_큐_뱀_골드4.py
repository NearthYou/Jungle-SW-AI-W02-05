# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

# N * N 정사각 보드
# 몇몇 칸에 사과 상하좌우 끝에 벽
# 이동한 칸에 사과 있으면 없어지고 꼬리는 움직이지 않음 -> 몸 길이가 늘어남
# 이동한 칸에 사과 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 몸 길이는 변하지 않음

# 뱀은 처음에 오른쪽을 향하고 길이는 1이다. 시작 점은 상단 좌측(0, 0)
# 매초마다 이동을 함

# 머리의 행동을 뒤에서 한 박자씩 늦게 따라함 그래서 큐로 진행
# 벽 끝 or 자기 몸에 닿으면 게임오버

# D -> 오른쪽 90도 회전
# L -> 왼쪽으로 90도 회전

# 이동할 떄 큐에 푸시
# 다음 차례에 팝
# 사과 있는 칸이면 팝 무시
# 팝 할 때, 인덱스를 가져오면 상태 변경할 수 있음
# -> 지나갈 때 2를 새겨서 지금 몸 혹은 꼬리가 있는 위치로 판단
# -> 팝할 때 인덱스 가져와서 다시 0으로 변경

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n = int(input())
matrix = [[0] * n for _ in range(n)]

apple_count = int(input())
for _ in range(apple_count):
    row, col = map(int, input().split())
    matrix[row-1][col-1] = 1

l_count = int(input())
commands = deque()
for _ in range(l_count):
    t, c = input().split()
    commands.append((int(t), c))

time = 0
r, c = 0, 0
direction = 1
matrix[r][c] = 2
snake = deque([(r, c)])

while True:
    nr = r + dr[direction]
    nc = c + dc[direction]
    time += 1

    if not (0 <= nr < n and 0 <= nc < n) or matrix[nr][nc] == 2:
        break

    if matrix[nr][nc] != 1:
        tr, tc = snake.popleft()
        matrix[tr][tc] = 0

    matrix[nr][nc] = 2
    snake.append((nr, nc))
    r, c = nr, nc

    if commands and time == commands[0][0]:
        _, turn = commands.popleft()
        if turn == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

print(time)