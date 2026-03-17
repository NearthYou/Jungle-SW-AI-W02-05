# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

# N 개의 자연수들로 이루어진 집합 U
# 이 중에서 적당히 세 수의 합 d도 U안에 포함되는 경우가 있을 수 있다.
# 이러한 경우들 중에서, 가장 큰 d를 찾으라

# 백트래킹?

n = int(input())
nums = [int(input()) for _ in range(n)]

sum_set = set()
for i in range(len(nums) - 1):
    for j in range(i, len(nums)):
        sum_set.add(nums[i] + nums[j])
nums = sorted(nums)

for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        k = nums[i]
        z = nums[j]
        if k - z in sum_set:
            print(k)
            exit()