# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

# N 개의 자연수들로 이루어진 집합 U
# 이 중에서 적당히 세 수의 합 d도 U안에 포함되는 경우가 있을 수 있다.
# 이러한 경우들 중에서, 가장 큰 d를 찾으라

# 백트래킹?


n = int(input())

nums = [int(input()) for _ in range(n)]
set_nums = set(nums)
max_num = 0
arr = []
def back_tracking(combi):
    global max_num
    if len(combi) == 3:
        sum_num = max(max_num, sum(combi))
        if sum_num in set_nums:
            max_num = max(max_num, sum_num)
        return
    
    for i in range(len(nums)):
        combi.append(nums[i])
        back_tracking(combi)
        combi.pop()

back_tracking(arr)
print(max_num)