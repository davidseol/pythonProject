class fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result

a = fourcal()
b = fourcal()
a.setdata(4,2)
b.setdata(3,8)

print(a.add())
print(a.mul())