# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

# 둘을 더했을 때 0에 가장 가까운 값 찾기

n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)

left = 0
right = len(nums) - 1
min_abs_sum = float('inf')
ans = [0, 0]

while left < right:
    current_sum = nums[left] + nums[right]
    
    if abs(current_sum) < min_abs_sum:
        min_abs_sum = abs(current_sum)
        ans = [nums[left], nums[right]]
    
    if current_sum < 0:
        left += 1
    elif current_sum > 0:
        right -= 1
    else:
        break

print(ans[0], ans[1])