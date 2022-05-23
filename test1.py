
#문자열 바꾸기
#a:b:c:d 와 같은 문자열이 있다. 문자열의 split와 join 함수를 사용해서 아래와 같이 고치시오
#a#b#c#d

aa = 'a:b:c:d'
b = aa.split(':')
c = '#'.join(b)
print(c)
