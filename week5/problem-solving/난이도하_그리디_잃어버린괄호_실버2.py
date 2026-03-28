# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

import sys

input = sys.stdin.readline
formula = input().rstrip()

sum_num = 0
formula = formula.split("-")

first = formula[0]
first_sum = 0
if "+" in first:
    first = map(int, first.split("+"))
    first_sum = sum(first)
else:
    first_sum = int(first)

others = formula[1:]
others_sum = 0
for c in others:
    if "+" in c:
        plus = map(int, c.split("+"))
        others_sum += sum(plus)
    else:
        others_sum += int(c)
    
print(first_sum - others_sum)

# words = input()

# negative_parts = words.split("-")
# result = sum(map(int, negative_parts[0].split("+")))

# for part in negative_parts[1:]:
#     result -= sum(map(int, part.split("+")))

# print(result)