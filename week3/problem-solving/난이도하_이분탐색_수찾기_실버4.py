# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

# 1~N 개의 정수가 주어졌을 때 X라는 정수가 존재하는 알아내는 프로그램을 작성

# M

import sys
input = sys.stdin.readline

# nums_a 안에 nums_m 요소가 있는지

def binary(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0


n = int(input().strip())
nums_a = list(map(int, input().split()))
nums_a = sorted(nums_a)

m = int(input().strip())
nums_m = list(map(int, input().split()))

for i in nums_m:
    print(binary(nums_a, i))