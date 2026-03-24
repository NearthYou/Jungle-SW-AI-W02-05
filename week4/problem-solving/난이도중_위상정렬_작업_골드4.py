# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

# from collections import deque

# def topological_sort(vertices, edges):
#     graph = [[] for _ in range(vertices)]
#     indegree = [0] * vertices

#     for u, v in edges:
#         for next in v:
#             graph[u].append(next - 1)
#             indegree[next - 1] += 1

#     q = deque()
#     for i in range(vertices):
#         if indegree[i] == 0:
#             q.append(i)
    
#     result = []
#     while q:
#         cur = q.popleft()
#         result.append(cur)

#         for next in graph[cur]:
#             indegree[next] -= 1

#             if indegree[next] == 0:
#                 q.append(next)
    
#     return result

# # 소요 시간, 작업 순서 담은 배열 생성
# n = int(input())

# s = []
# for _ in range(n):
#     s.append(list(map(int, input().split())))

# w = []
# for i in range(n):
#     temp = []
#     for j in range(2, s[i][1] + 2):
#         temp.append(s[i][j])
#     w.append((i, temp))

# # 2번 배열을 대상으로 위상정렬
# result = topological_sort(n, w)
# print(result)
# sum_result = 0
# for i in range(n):
#     sum_result += s[result[i]][0]

# print(sum_result)
# # 이후 1번 배열에서 소요 시간 접근해서 더하기

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]

    if data[1] > 0:
        for prev in data[2:]:
            graph[prev].append(i)
            indegree[i] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = time[i]

while q:
    cur = q.popleft()

    for next_node in graph[cur]:
        indegree[next_node] -= 1

        dp[next_node] = max(dp[next_node], dp[cur] + time[next_node])

        if indegree[next_node] == 0:
            q.append(next_node)

print(max(dp))

# import sys
# input = sys.stdin.readline

# n = int(input())

# # 각 작업이 완료되는 최소 시간을 저장할 리스트
# dp = [0] * (n + 1)

# for i in range(1, n + 1):
#     data = list(map(int, input().split()))
    
#     time = data[0]      # 현재 작업 소요 시간
#     num_pre = data[1]   # 선행 작업 개수
    
#     # 선행 작업이 없다면 바로 자신의 시간이 완료 시간
#     if num_pre == 0:
#         dp[i] = time
#     else:
#         # 선행 작업들 중 가장 늦게 끝나는 시간 찾기
#         max_prev_time = 0
#         for j in range(2, 2 + num_pre):
#             pre_task = data[j]
#             max_prev_time = max(max_prev_time, dp[pre_task])
        
#         # 현재 작업 완료 시간 = 선행 최대 시간 + 내 시간
#         dp[i] = max_prev_time + time

# # 모든 작업 중 가장 마지막에 끝나는 작업의 시간이 정답
# print(max(dp))