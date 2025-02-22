class First: pass
class Second(First): pass
class Third(Second): pass

one = First()
two = Second()
three = Third()

# функция isinstance(obj, cls) возвращает True, если объект obj является объектом класса cls но не его базовых классов
print(isinstance(three, First)) # True Утверждение неверное.
# функция isinstance(cls1, cls2) возвращает True, если класс cls1 является подклассом класса cls2 или какого-либо его базовых классов
print(isinstance(Third, First)) # False Утверждение неверное.
# функция issubclass(obj, cls) возвращает True, если объект obj является объектом класса cls или какого-либо его базовых классов
print(issubclass(three, First)) # TypeError: issubclass() arg 1 must be a class Утверждение неверное.
# функция issubclass(cls1, cls2) возвращает True, если класс cls1 является подклассом класса cls2 но не его базовых классов
print(issubclass(Third, First)) # True Утверждение неверное.