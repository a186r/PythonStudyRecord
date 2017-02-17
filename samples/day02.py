# 1. 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 2. 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# 3. 在python中定义函数，5种参数可以组合使用，但是顺序必须是：必选参数，默认参数，可变参数，命名关键字参数和关键字参数
# 4. 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

# !/usr/bin/python
# -*- coding: UTF-8 -*-


# import math

# def my_abs(x):
#     if not isinstance(x,(int , float)):
#         raise TypeError('Type Error')
#     if x > 0:
#         return x;
#     else :
#         return -x;

# # p(my_abs('s'))

# def nop():
#     pass

# def move(x,y,step,angle = 0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx,ny

# # p(move(100,100,60,math.pi/6))

# def power(x,n = 2): # 默认参数／必选参数在前，默认参数在后，否则Python的解释器会报错
#     s = 1;
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# # print(power(2))

# def enroll(name,gender,age = 6,city = 'Beijing'):
#     print(name)
#     print(gender)
#     print(age)
#     print(city)

# # enroll('Lida','A+')

# # enroll('Dursss','S+',city = 'GanSu',age = 14)

# def add_end(L = None):# 利用None这样的不变对象来做默认参数
#     if L == None:
#         L = []
#     L.append('END')
#     return L

# # print(add_end())

# def calc(*numbers): #前面加*号可以传可变参数进去
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# nums = [1,3,5]

# print(calc(*nums)) # *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

# def person(name,age,**kw):
#     print('name:',name,'age:',age,'others:',kw)

# extra = {'city':'US','Job':'Engineer','gender':'S+'}
# # person('dursss',12,gender = extra['gender'], city = extra['city'],Job = extra['Job']) # 可以传入任意个数的关键字参数，这些关键字参数自动组装为dict

# person('dursss',23,**extra)# 上面复杂调用的简化写法，**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict
# # ，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

# extra = {'city':'UA','Job':'Engineer','gender':'S+'}
# def person(name,age,*,city,gender): # 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数

#     print(name,age,city,gender)

# person('dursss',24,city ='US',gender = 'S') # 命名关键字参数调用方式

# def person(name,age,*job,gender): # 如果函数定义中已经有了一个可变参数，那么后面跟着的命名关键字参数就不需要有特殊分隔符了
# # def person(name,age,*,job = 'Engineer',gender = 'S+') #命名关键字参数可以有缺省值，从而可以简化使用
#     print(name,age,job,gender)

# person('dursss',14,'Engineer',gender = 'S+')

# def f1(a,b,c = 0,*args,**kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# def f2(a,b,c = 0, * ,d,**kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# # f1('a','c',12,'a','d',**{'name':'dursss'})
# # f2(1,2,d = 99, c= 10,** {'1':'2'})

# args = (1,2,3,5,123,4)
# kw = {'d':12,'g':53}

# f1(*args,**kw) # 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

# args = (1,2,3) 
# kw = {'d': 88, 'x': '#'}
# f2(*args,**kw)

# ==================================================小结=======================================================

    # 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！                

    # 要注意定义可变参数和关键字参数的语法：                                         

    # *args是可变参数，args接收的是一个tuple；                                     

    # **kw是关键字参数，kw接收的是一个dict。

    # 以及调用函数时如何传入可变参数和关键字参数的语法：

    # 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

    # 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

    # 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

    # 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

    # 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

### 递归函数

# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

# 1. 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)
# 2. 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 3. 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

# def fact(n):
#     if n == 1:
#         return 1;
#     return n*fact(n-1)

# print(fact(998))

# 改进后的代码

# def fact(n):
#     return fact_iter(n,1)

# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1 , num * product)

# print(fact(900))
    
# 重点来了，遗憾的是，很多编译器并没有对尾递归做优化，python也一样，所以，即使用了尾递归，也还是无法避免栈溢出 :)
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

# 汉诺塔的移动可以很方便的使用递归来解决

# def move(n,a,b,c):
#     if n == 1:# 当只有一个盘子的时候，直接从A移动到C
#         print(a,'-->',c)
#     else:
#         move(n-1,a,c,b) # 从a移动n-1个到b
#         print(a,'-->',b)
#         move(n-1,b,a,c) # b的n-1个移动到c

# move(4,'A','B','C')





























