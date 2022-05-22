
# 게시판 페이징하기
# 게시물의 총 건수와 한페이지에 보여줄 게시물 수를 입력으로 주었을떄 총 페이지수?

def gettotalpage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(gettotalpage(5, 10))
print(gettotalpage(15, 10))
print(gettotalpage(25, 10))
print(gettotalpage(30, 10))