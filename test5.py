

# 피보나치 함수
# 첫번째 항의 값이 0이고 두번째 항의 값이 1일때, 이후에 이어지는 항은 이전의 두항을 더한 값으로 이루어지는 수열이 피보나치
# 입력을 정수 n으로 받았을 때 n이하까지의 피보나치 수열을 출력하는 함수 작성해보자.

def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-2) + fibo(n-1)
for i in range(10):
    print(fibo(i))