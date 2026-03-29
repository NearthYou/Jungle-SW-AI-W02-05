# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

import sys
input = sys.stdin.readline

# n, m
# 두 정수 n, m을 받는다.
n, m = map(int, input().split())
limits = int((2 * n) ** 0.5) + 2

# set으로 건너 뛸 지점 받는다
small = set()
for _ in range(m):
    small.add(int(input()))

# dp[위치][속도]
dp = [[float('inf')] * limits for _ in range(n + 1)]

# 두번째 돌은 무조건 한칸 
if 2 not in small:
    dp[2][1] = 1

# 가만히 있거나, 1칸 가거나, 뒤로 1칸 가거나
for i in range(3, n + 1):
    if i in small:
            continue
    for j in range(1, limits - 1):
         dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
 
ans = min(dp[n])
print(ans if ans != float('inf') else -1)



















# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# # dp[위치][속도], 속도 최대치는 약 141 (루트 2*10000)
# limit = int((2 * n) ** 0.5) + 2
# dp = [[float('inf')] * limit for _ in range(n + 1)]

# # 못 가는 돌 처리
# traps = set()
# for _ in range(m):
#     traps.add(int(input()))

# # 초기 상태: 1번 돌에서 2번 돌로 크기 1로 점프
# if 2 not in traps:
#     dp[2][1] = 1

# for i in range(3, n + 1):
#     if i in traps:
#         continue
    
#     for v in range(1, limit - 1):
#         # i위치에 v속도로 도달하려면 이전(i-v)에서 v-1, v, v+1 속도로 왔어야 함
#         dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1

# ans = min(dp[n])
# print(ans if ans != float('inf') else -1)

# =================================================

# import sys
# from collections import deque

# input = sys.stdin.readline

# def solve():
#     n, m = map(int, input().split())
    
#     # 장애물 처리
#     traps = set()
#     for _ in range(m):
#         traps.add(int(input()))
        
#     # visited[위치][속도] -> 해당 상태에 도달한 적이 있는지 체크
#     limit = int((2 * n) ** 0.5) + 2
#     visited = [[False] * limit for _ in range(n + 1)]
    
#     # queue: (현재 위치, 현재 속도, 점프 횟수)
#     queue = deque()
    
#     # 초기 상태: 1번에서 시작해 2번으로 점프 (속도 1, 횟수 1)
#     if 2 not in traps and n >= 2:
#         queue.append((2, 1, 1))
#         visited[2][1] = True
        
#     while queue:
#         curr_i, curr_v, count = queue.popleft()
        
#         # 목표 지점 도달 시 바로 리턴 (BFS 특성상 이게 최솟값임)
#         if curr_i == n:
#             print(count)
#             return

#         # 다음 속도 후보: v-1, v, v+1
#         for dv in [-1, 0, 1]:
#             next_v = curr_v + dv
#             next_i = curr_i + next_v
            
#             # 이동 가능 조건 확인
#             if next_v > 0 and next_i <= n:
#                 if next_i not in traps and not visited[next_i][next_v]:
#                     visited[next_i][next_v] = True
#                     queue.append((next_i, next_v, count + 1))
                    
#     print(-1)

# solve()