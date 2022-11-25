# 재귀 방식
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid]> target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)

# 반복문 방식
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid]> target:
#             end = mid - 1
#         else:
#             start = mid + 1


# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n - 1)
# if result == None:
#     print('원소가 없습니다.')
# else:
#     print(result+1)

# ex)
# 요청한 총 길이가 M일 때 적어도 M 만킁의 떡을 얻기 위해 절단기 설정할 수 있는 최대 높이값 구하기
# 파라메트릭 서치는 최적화 문제를 결정 문제로 바꾸어 해결하는 기법

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split(' ')))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1
print(result)










