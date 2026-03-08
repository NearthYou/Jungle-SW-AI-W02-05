# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

nums = list()
for i in range(9):
    num = int(input())
    nums.append(num)

max_num = max(nums)
max_index = nums.index(max_num)

print(max_num)
print(max_index + 1)