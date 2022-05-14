treehit=0
while treehit<10:
    treehit=treehit+1
    print('나무를 %d번 찍었습니다.' %treehit)
    if treehit == 10:
        print('나무 넘어갑니다.')



def solution(n):
    answer=0
for i range(1,10001):
    answer+=i
    if i%2==0:
        answer.append('박')
    else:
        answer.append('수')
    return answer









