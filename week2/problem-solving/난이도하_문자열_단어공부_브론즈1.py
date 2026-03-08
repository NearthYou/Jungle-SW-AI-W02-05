# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

word = input()
word = word.lower()
counting = {}

for c in word:
    # 문자 나타날 때 딕셔너리에 있는지 확인 후 있으면 밸류 값 증가
    if c in counting:
        counting[c] += 1
    else:
        counting[c] = 1

max_count = max(counting.values())

result = []
for char, count in counting.items():
    if count == max_count:
        result.append(char)

if len(result) > 1:
    print("?")
else:
    print(result[0].upper())