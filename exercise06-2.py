
# 3과 5의 배수 합하기
# 1000미만의 자연수에서 3의배수와 5의배수의 총합을 구하라.

result = 0
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)