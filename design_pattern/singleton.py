# coding: utf-8

# 使用类变量实现单例模式

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# 使用类装饰器实现单例模式
def singleton(cls):
    instance = []

    def f(*args, **kwargs):
        if not instance:
            instance.append(cls())
        return instance[0]
    return f


@singleton
class A:
    pass

def test():
    a = Singleton()
    b = Singleton()
    print(id(a), id(b))
    print(a is b)
    c = A()
    d = A()
    print(id(c), id(d), c is d)

if __name__ == '__main__':
    test()
