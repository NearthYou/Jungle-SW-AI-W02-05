# DP - 외판원 순회 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/2098

# 한 번 갔던 도시에는 다시 갈 수 없다.
# 도시 간에 이동하는데 드는 비용은 행렬 W[i][j] 형태로 주어진다. 
# 비용은 대칭적이지 않다. 오고 가는 비용이 다르다는 뜻.
# 모든 비용은 양의 정수, 갈 수 없는 경우 비용 0
# 최소 비용을 출력한다

import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (1 << n) for _ in range(n)]

def tsp(now, visited):
    # 1. 모든 도시를 방문한 경우 (기저 사례)
    if visited == (1 << n) - 1:
        # 시작점(0번)으로 돌아가는 길이 있다면 그 비용을, 없다면 무한대를 반환
        return matrix[now][0] if matrix[now][0] != 0 else float('inf')

    # 2. 이미 계산한 적이 있는 경우 (메모이제이션)
    if dp[now][visited] != -1:
        return dp[now][visited]

    # 3. 다음 도시들 탐색
    min_cost = float('inf')
    for next_node in range(n):
        # 아직 방문하지 않았고, 갈 수 있는 길이 있다면?
        if not (visited & (1 << next_node)) and matrix[now][next_node] != 0:
            # 재귀적으로 다음 비용을 계산
            cost = tsp(next_node, visited | (1 << next_node)) + matrix[now][next_node]
            min_cost = min(min_cost, cost)

    dp[now][visited] = min_cost
    return min_cost

# 시작은 0번 도시에서, 0번 도시를 방문한 상태(1 << 0)로 출발!
print(tsp(0, 1 << 0))