# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

# 글자 두개를 입력받고 쪼개서 리스트를 만든다.

# dp를 저장한 배열을 만든다

# 길이를 입력받는다. n m

# 이중 반복문을 돌린다 1 -> n까지

# 밑에 1 -> m까지

# 첫 번째 문자열과 두 번째 문자열이 같을 때, 왼쪽 대각선에 있는 것 + 1 해줌

# 안 같으면 이전꺼랑 비교해서 더 큰 값 넣어버림

import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

n ,m = len(s1), len(s2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])

# 공통요소 출력

# result = []
# i, j = n, m

# while i > 0 and j > 0:
#     if s1[i - 1] == s2[j - 1]:
#         result.append(s1[i - 1])
#         i -= 1
#         j -= 1
#     else:
#         if dp[i - 1][j] >= dp[i][j - 1]:
#             i -= 1
#         else:
#             j -= 1

# print("".join(reversed(result)))


# 롤링 어레이 최적화

# # 1차원 배열을 이용한 공간 최적화 (LCS 길이만 구할 때)
# def lcs_optimized_space(s1, s2):
#     n, m = len(s1), len(s2)
#     if n < m: # 짧은 문자열을 기준으로 배열 생성 (공간 최소화)
#         s1, s2 = s2, s1
#         n, m = m, n

#     dp = [0] * (m + 1)

#     for char1 in s1:
#         prev_upper_left = 0 # dp[i-1][j-1] 역할
#         for j in range(1, m + 1):
#             temp = dp[j] # 현재 dp[j]는 다음 루프의 prev_upper_left가 됨
#             if char1 == s2[j-1]:
#                 dp[j] = prev_upper_left + 1
#             else:
#                 dp[j] = max(dp[j], dp[j-1])
#             prev_upper_left = temp
#     return dp[m]