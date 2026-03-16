# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

# 문자를 뒤집어도 비밀번호로 사용 가능
# 단어가 주어지면 길이와 가운데 글자를 출력하는 프로그램 작성

# 출력 : 첫째 줄에 단어의 수 N, 다음 N개의 줄에는 파일에 적혀있는 단어가 한 줄에 하나씩 주어짐
# 입력: 첫째 줄에 비밀번호의 길이와 가운데 글자를 출력

# 뒤집었을 때, 목록에 존재하는가?를 보면 됨
# 그리고 가운데 글자를 가져오기

n = int(input())

result = []
for _ in range(n):
    pw = input()
    result.append(pw)

pw_len = 0
pw_middle = ""
for i in result:
    if i[::-1] in result:
        pw_len = len(i)
        pw_middle = i[pw_len // 2]
        break

print(f"{pw_len} {pw_middle}")