def func1():
    raise TypeError("ошибка")

try:
    a = 10/0
    func1()
except TypeError:
    print("continue")
except ZeroDivisionError:
    print("continue")
finally:
    print("finally")
