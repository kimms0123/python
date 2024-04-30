# 정수 n에 따른 수열 합산 퀴즈
# 정수 n을 매개변수로 받아들여, n의 홀짝 성에 따라 다른 계산을 수행하는 프로그램을 작성하라.
# n이 홀수 일시 n이하의 모든 홀수의 합을 반환/ 짝수라면 n이하의 모든 짝수의 제곱의 합 반환
# num = int(input("정수 입력>>"))
# result = 0
#
# # 홀수
# if num % 2 != 0:
#     for x in range(num+1):
#         if x % 2 == 1:
#             result += x
#     print(result)
# # 짝수
# else:
#     for x in range(num + 1):
#         if x % 2 == 0:
#             result += x ** 2
#     print(result)

# 배열 변환 기반 조건적 연산 퀴즈
# 정수 배열 arr과 자연수 k가 주어졌을 시, k의 홀짝성에 따라 배열에 다른 연산을 적용한다.
# 만약 k가 홀수라면 배열 arr의 모든 원소에 k를 곱하고, 짝수라면 모든 원소에 k를 더한다.
# arr = [1, 2, 3]
# k = int(input("k입력>>"))
# result = []
#
# if k % 2 != 0:
#     for x in arr:
#         result.append(x * k)
# else:
#     for x in arr:
#         result.append(x + k)
# print(result)

