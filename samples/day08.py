# 函数对象有一个__name__的属性，可以拿到函数的名字

# def now():
#     print('2017-02-28')
#
#
# f = now
#
# print(f())
# print(now.__name__)
# print(f.__name__)
#

# 现在，假设我们要增强now函数的功能，比如在函数调用前后自动打印日志，但又不希望修改now函数的定义
# ，这种在代码运行期间动态增加功能的方式，称之为装饰器(Decorator)

# 本质上，decorator就是一个返回函数的高阶函数，所以，我们要定义一个能打印日志的decorator就可以定义如下
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2017-02-28')

print(now())

# 把@log放在now函数的定义处，相当于执行了语句
now = log(now)