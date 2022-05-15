a=60
b=75
c=55
print(a+b+c/3)


# 돌아가는 코드로 짜서 만들어라

#while문을 사용해서 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자.

result=0
i=1
while i<=1000:
    if i%3 ==0:
        result+=i
print(result)



