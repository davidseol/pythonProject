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

def say_myself(name,old,man=True):
    print('나의 이름은 %s 입니다.' %name)
    print('나이는 %d살입니다.' %old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')
    say_myself('설창환',33)

f=open('새파일.txt','w')
for i in range(1,11):
    data='%d번쨰 줄입니다.\n' %i
    f.write(data)
f.close()


f=open('새파일.txt','r')
line=f.readline()
pritn(line)
f.close()


#mod1.py
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

try:
    aa=[1,2]
    print(aa[3])
    4/0
except exception:
    print('0으로 나눌 수 없습니다')
except exception:
    print('인덱싱 할 수 없습니다')

try:
    f=open('나없는파일','r')
except exception:
    pass

class Bird:
    def fly(self):
        raise exception
class Eagle(Bird):
    def fly(self):
        print('very fast')