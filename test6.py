
# 숫자의 총합 구하기

# 사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오
                                                                   #(단, 숫자는 콤마로 구분하여 입력한다.)

a = input('숫자를 입력하세요: ')
numbers = a.split(',')
total = 0
for i in numbers:
    total += int(i)
print(total)