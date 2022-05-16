
# '주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라'는 문장을 조건문으로 만들어 보자.

pocket = ['card', 'id', 'money']     # 포켓안에 리스트는 임의로 내가 지정했습니다

if 'card' not in pocket:
    print('걸어가라')

else:
    print('버스를 타고 가라')
