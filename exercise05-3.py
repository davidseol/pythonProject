class fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result

a = fourcal(4,2)
b = fourcal(3,6)


print(a.add())
print(a.mul())
print(b.add())

class morefoulcal(fourcal):
    def pow(self):
        result = self.first ** self.second
        return result
a = morefoulcal(4, 2)
print(a.pow())