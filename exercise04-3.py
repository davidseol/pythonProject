

#다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.

input1 = input('첫번쨰 숫자를 입력하세요: ')
input2 = input('두번째 숫자를 입력하세요: ')

total = input1 + input2
print('두 수의 합은 %s 입니다' % total)


#수정 ------ input은 입력값을 문자로 취급하니 int함수 사용!

input1 = input('첫번쨰 숫자를 입력하세요: ')
input2 = input('두번째 숫자를 입력하세요: ')

total = int(input1) + int(input2)
print('두 수의 합은 %s 입니다' % total)