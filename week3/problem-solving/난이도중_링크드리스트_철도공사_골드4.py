# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

# 역의 개수 N 공사 횟수 M 
# 역의 고유 번호 리스트
# 명령어 i j

# BN -> i 다음역 출력, 그 사이에 j역 설립
# BP -> i 이전역 출력, 그 사이에 j역 설립
# CN -> i 다음역 폐쇄, 출력
# CP -> i 이전역 폐쇄, 출력

# 폐쇄 작업은 2개 이상일 때만 들어오고, 중복 설립 없음

n, m = map(int, input().split())
nums = list(map(int, input().split()))

next_node = [0] * 1000000
prev_node = [0] * 1000000

for i in range(len(nums)):
    prev = i - 1
    next = i + 1
    if prev < 0:
        prev = len(nums) - 1
    if next >= len(nums):
        next = 0
    next_node[nums[i]] = nums[next]
    prev_node[nums[i]] = nums[prev]

rs = []
for num in range(m):
    com_list = list(input().split())
    com = com_list[0]
    i = int(com_list[1])
    match com:
        case "BN":
            # 다음꺼 저장
            j = int(com_list[2])
            nexts = next_node[i]
            prev_node[j] = i
            prev_node[nexts] = j
            next_node[j] = nexts
            next_node[i] = j
            rs.append(nexts)
        case "BP":
            j = int(com_list[2])
            prevs = prev_node[i]
            next_node[j] = i
            next_node[prevs] = j
            prev_node[j] = prevs
            prev_node[i] = j
            rs.append(prevs)
        case "CN":
            nexts = next_node[i]
            next_node[i] = next_node[nexts]
            prev_node[next_node[nexts]] = i
            rs.append(nexts)
        case "CP":
            prevs = prev_node[i]
            prev_node[i] = prev_node[prevs]
            next_node[prev_node[prevs]] = i
            rs.append(prevs)

for i in rs:
    print(i)