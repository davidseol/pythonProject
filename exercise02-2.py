#while문을 사용해서 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자.

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
print(result)                 #결과값이 안뜨는데 i가 3의배수가 다 더해진 상태이고 그걸 result에 담았는데 어디가 잘못된지 모르겠어요



