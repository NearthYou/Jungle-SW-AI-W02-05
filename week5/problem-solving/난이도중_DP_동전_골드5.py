# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

# 1. T는 테스트 케이스의 개수
t = int(input())
# T만큼 아래를 반복
# -1 동전의 가짓 수 N
# -2 N가지 동전 각 금액이 오름차순으로 주어진다
# -3 만들어야 할 금액
rs = []
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    rs.append(dp[target])

print(rs)

# N 가지 동전으로 금액 M 을 만드는 모든 방법의 수
# 0원부터 목표 금액 M 원까지 담을 수 있는 dp 배열 만들기
# dp[0] = 1로 설정하기

# 사용할 수 있는 동전들을 하나씩 꺼내기

# 금액 갱신하기