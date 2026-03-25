# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

from collections import deque

def solve():
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        num = int(input())
        coins.append(num)

    visited = [False] * (k + 1)
    queue = deque()

    def bfs():
        queue.append((0, 0))
        visited[0] = True

        while queue:
            money, count = queue.popleft()

            if money == k:
                print(count)
                return

            for coin in coins:
                next_money = money + coin

                if next_money <= k and not visited[next_money]:
                    visited[next_money] = True
                    queue.append((next_money, count + 1))
        print(-1)

    bfs()
solve()

# import sys

# def solve():
#     # n: 동전 종류 수, k: 목표 금액
#     input_data = sys.stdin.read().split()
#     if not input_data:
#         return
    
#     n, k = map(int, input_data[:2])
#     # set으로 중복 제거 후 리스트화
#     coins = list(set(map(int, input_data[2:])))
    
#     # 1. dp 배열 초기화 (k+1 크기, 충분히 큰 값으로)
#     # k가 최대 10,000이므로 10,001은 "불가능"을 의미하는 충분히 큰 수입니다.
#     dp = [10001] * (k + 1)
#     dp[0] = 0  # 0원을 만드는 개수는 0개
    
#     # 2. 동전을 하나씩 꺼내어 dp 테이블 갱신
#     for coin in coins:
#         for i in range(coin, k + 1):
#             # i원 - 현재 동전 가치를 뺀 금액을 만들 수 있다면 최솟값 갱신
#             if dp[i - coin] != 10001:
#                 dp[i] = min(dp[i], dp[i - coin] + 1)
    
#     # 3. 결과 출력
#     if dp[k] == 10001:
#         print(-1)
#     else:
#         print(dp[k])

# solve()