# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

n = int(input())

avg_list = list()
for i in range(n):
    nums = list(map(int, input().split()))

    std_cnt =  nums[0]
    scores = nums[1:]

    average = sum(scores) / std_cnt

    avg = [s for s in scores if s > average]
    avg_ratio = len(avg) / std_cnt * 100
    avg_list.append(avg_ratio)

for avg in avg_list:
    print(f"{avg:.3f}%")