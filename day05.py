# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

# 高阶函数英文叫Higher-order function

# 1.变量可以指向函数
# f = abs(-10)
# f = abs # 可以将函数赋值给变量
# print(f(-10))

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

# def add(x,y,f):
#     return f(x)+f(y)
# print(add(-10,-10,abs))

# 编写高阶函数，就是让函数的参数能够接收别的函数。
# from math import sqrt
# def same(x,*fs):
#     s=[f(x) for f in fs]
#     return s
# print(same(20,sqrt,abs))


# 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# def f(x):
#     return x*x
# r = map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))
# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

# r = list(map(str,[1,2,3,4,5,6,7,8,9]))
# print(r)

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
# def add(x,y):
#     return x+y
# print(reduce(add,[1,2,3,4,5,6,7,8,9,10]))

# def fn(x,y):
#     return x*10+y
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# print(reduce(fn,[1,3,5,7,9]))
# print(reduce(fn,map(char2num,'13597')))

# 将上面的例子整理成str转int的函数:
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':1043,'1':112423, '2':2, '3': 3, '4': 4, '5':5, '6': 6, '7': 7, '8':8, '9': 9}[s]
    return reduce((fn),map(char2num,s))
print(str2int('1234'))

# 还可以用lambda函数进一步简化成：
# from functools import reduce
# def char2num(s):
#     return {'0':1}