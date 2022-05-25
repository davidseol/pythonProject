
# 사칙연산 계산기
# 다음과 같이 동작하는 클래스 calculator를 작성하시오.

class Calculator:
    def __init__(self, first):
        self.first = first
    def sum(self):
        result = 0
        for num in self.first:
            result += num
        return result

    def avg(self):
        total = self.sum()
        return total / len(self.first)

cal1 = Calculator([1, 2, 3, 4, 5])
cal1.sum()
cal1.avg()
