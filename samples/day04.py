# d = {'a':1,'b':2,'c':3}
# for key in d:
# for value in d.values():
# for k,v in d.items():
    # print(value)

# for ch in 'ACAFCSVABDGYFTYC':# 迭代字符串
    # print(ch)

# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

# from collections import Iterable # 导包
# print(isinstance('absaksd',Iterable)) # 判断对象是否可迭代

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成 索引-元素对 ，这样就可以在for循环中同时迭代索引和元素本身：

# for i,value in enumerate(['A','B','C']):
#     print(i+ord(value))

# for x,y in [(1,2),(3,5),(8,9)]:
#     print(x,y)

# 任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。

# L = list(range(1,11))
# print(L)

# L = []
# for x in range(1,11):
#     L.append(x*x)

# print(L)

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

# L = [x * x for x in range(1,12)] # 列表生成式

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
# L = [x * x for x in range(1,12) if x % 2 == 0] 

# 还可以使用两层循环，可以生成全排列：
# L = [x+x for x in 'ABC' for n in 'GHJ']
# print(L)

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
# import os # 导入os模块
# L = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
# print(L)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
# d = {'X':'A','Y':'B','Z':'C'}
# for k,v in d.items():
#     print(k,v)

# 因此，列表生成式也可以使用两个变量来生成list：
# d = {'X':'A','Y':'B','Z':'C'}
# L = [k+'='+v for k,v in d.items()]
# print(L)

# 最后把一个list中所有的字符串变成小写
# L = ['HELLO','WORLD','IBM','GOOGLE','APPLE']
# L = ['HELLOW',12,'WORLD']# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# l = [s.lower() for s in L]
# print(l)

# 使用内建的isinstance函数可以判断一个变量是不是字符串
# x = 'abc'
# y = 123

# print(isinstance(x,str))
# print(isinstance(y,str))

# L1 = ['HELLO','WORLD',18,'APPLE',None]
# L2 = []
# for x in L1:
#     if isinstance(x,str):
#         L2.append(x.lower())
# print(L2)
        
