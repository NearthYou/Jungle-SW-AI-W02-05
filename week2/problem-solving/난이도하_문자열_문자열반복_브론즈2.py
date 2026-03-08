# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

n = int(input())

str_list = list()
for i in range(n):
    arr = list(map(str, input().split()))

    cnt = int(arr[0])
    string = arr[1]

    result = ""
    for char in string:
        result += char * cnt
    str_list.append(result)

for string in str_list:
    print(string)