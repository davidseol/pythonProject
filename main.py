def is_odd(number):
    if number%2 == 1:
        return True
    else:
        return False
print(is_odd(3))
print(is_odd(4))

def avg_numbers(*args):
    result=0
    for i in args:
        result += i
    return result / len(args)
print(avg_numbers(1,2))
print(avg_numbers(2,4,9))

input1=input("첫 번쨰 숫자를 입력하세요:")
input2=input("두 번쨰 숫자를 입력하세요:")
total=int(input1)+int(input2)

print("두수의 합은 %s 입니다" %total)

result1=0
result2=0
def add1(num):
    global result1
    result1 += num
    return result1
def add2(num):
    global result2
    result2 += num
    return result2
print(add1(3))
print(add1(4))
print(add2(3))
print(add2(9))



class fourcal:
    pass
a=fourcal()
type(a)

class fourcal:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result

a=fourcal()
a.setdata(4,2)
print(a.add())

a=fourcal()
b=fourcal()
a.setdata(4,2)
b.setdata(3,8)
print(a.add())
print(a.mul())












