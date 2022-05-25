

# 평균값 구하기
# 오른쪽과 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 구한후
# 평균값을 result.txt 파일에 쓰는 프로그램을 작성하시오.

f = open('sample.txt')
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score
average = total / len(lines)

f = open('result.txt', 'w')
f.write(str(average))
f.close()
