# -*- coding: utf-8 -*-

# date:2017-02-16

# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 例如，在一个list中删掉偶数，保留奇数，如下：
# def is_odd(n):
#     return n%2 ==1
# print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

# 例如，把一个序列中的空字符串删掉，可以这么写：
# def no_empty(s):
#     return s and s.strip()
# print(list(filter(no_empty,['A','','B','C','','D'])))

# 可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。


# 用filter求素数：
# 计算素数的一个方法是【埃氏筛法】，它的算法理解起来非常简单：

# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 不断筛下去，就可以得到所有的素数。
# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：

# def _odd_iter(): # 注意这是一个生成器，并且是一个无限序列。
#     n = 1
#     while True:
#         n = n+2
#         yield n

# 然后定义一个筛选函数：
# def _not_divisible(n):
#     return lambda x:x%n>0

# 最后，定义一个生成器，不断返回下一个素数：
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible,it) # 构造新数列

# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
# l = []
# for n in primes():
#     if n< 1000:
#         print(n)
#         l.append(n)
#     else:
#         break

# print(len(l))

# TODO 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：


# 首先你要理解埃氏筛法的原理，其实是很简单的。
#
# 然后用惰性序列实现埃氏筛法时，只能想象抽象过程，不能推导每一步计算机是怎么算的，就像神经网络模拟的人工智能算法，连设计者也无法理解计算机执行的步骤。

# 排序算法 Python内置的sorted()函数就可以对list进行排序
# l = [1,23456,643,324,6,3,66,37,327,8,0]
# print(sorted(l))

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
# l = [1,-6,0,328,2,-40,-8,-67,-54]
# print(sorted(l,key = abs))

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list
# 然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素

# 默认情况下会根据首字母的ASCII码排序
# s = ['asbg','tr','erfv','Zweq','oiiy','Qwb','mcoi','qowiyt']
# print(sorted(s))
# 由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面

# 现在我们需要忽略大小写，只需要传入一个key作为规则就可以
# s = ['asbg','tr','erfv','Zweq','oiiy','Qwb','mcoi','qowiyt']
# print(sorted(s,key = str.lower))

# 要该用反向排序，不用改动key，只需要再传入一个reverse = True即可
# s = ['asbg', 'tr', 'erfv', 'Zweq', 'oiiy', 'Qwb', 'mcoi', 'qowiyt']
# print(sorted(s, key=str.lower, reverse=True))  # 忽略大小写并且倒序

# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。

# TODO 假设我们用一组tuple表示学生名字和成绩：L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)] 请用sorted()对上述列表分别按名字排序

# from operator import itemgetter
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
#
# def _by_name(t):  # 根据名字排序
#     return t[0]
#
#
# def _by_score(t):  # 根据成绩排序
#     return t[1]
#
#
# print(sorted(L, key=itemgetter(0)))  # 根据名字排序
# print(sorted(L, key=lambda t: t[1]))  # 根据成绩排序
# print(sorted(L, key=itemgetter(0), reverse=True))  # 根据名字倒序
# print(sorted(L,key = _by_name))
# print(sorted(L,key = _by_score))

# 返回函数 函数作为返回值

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# def calc_sum(*args):
#     ax = 0;
#     for n in args:
#         ax = ax + n
#     return ax

# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：

# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#
#     return sum


# # print(lazy_sum(1, 2, 3))  # 当我们调用lazy_sum的时候，返回的并不是求和结果，而是求和函数
# l = lazy_sum(2, 4)
# print(l())  # 当我们调用l的时候，才真正计算求和的结果

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量。
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# f1 = lazy_sum(1, 23, 4)
# f2 = lazy_sum(1, 23, 4)
# print(f1 == f2)  # 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数，f1和f2的调用结果互不影响

# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：

# def count():
#     fs = []
#     for i in range(1, 4):  # range 从1开始小于4 [1,2,3]
#         def f():
#             return i * i
#
#         fs.append(f)
#     return fs
#
#
# f1, f2, f3 = count()
#
# print(f1())
# print(f2())
# print(f3())

# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

# def count():
#     def f(j):
#         def g():
#             return j * j
#
#         return g
#
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs
#
#
# f1, f2, f3 = count()
#
# print(f1())
# print(f2())
# print(f3())

# 缺点是代码较长，可利用lambda函数缩短代码
# 小结：一个函数可以返回一个计算结果，也可以返回一个函数，
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的量
