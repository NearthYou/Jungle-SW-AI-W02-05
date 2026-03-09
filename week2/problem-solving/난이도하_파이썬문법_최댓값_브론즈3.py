# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

nums = list()
for i in range(9):
    n = int(input())
    nums.append(n)

max_num = max(nums)
max_idx = nums.index(max_num)

print(max_num)
print(max_idx)