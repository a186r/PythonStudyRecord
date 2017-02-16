#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import time;  # 引入time模块

# 1. ASCII 编码是 1 个字节
# 2. Unicode 编码通常是 2 个字节
# 3. UTF-8会把Unicode字符根据不同的数字大小编成1-6个字节，常用的英文字母被编成1个字节，汉字通常是3个字节
# ，只有很生僻的字符才被编成4-6个字节,如果要传输的文本包含大量英文字符，用UTF-8编码就能节省空间。ASCII码实际上可以看成是UTF-8的一部分
# 4. 在计算机内存中，统一使用Unicode编码，保存为文件或者需要传输的时候就转换为UTF-8编码
# 5. 网页源码：<meta charset="UTF-8" />

### python的编码

# 1. python字符串支持多语言 print("tou疼的字符串Str");
# 2. python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
# 3. 如果知道字符的整数编码，还可以用十六进制这么写    print('\u4e2d\u6587');

# 4. python对bytes类型的数据用带b前缀的单引号或双引号表示 x = b 'ABC';
# 5. 如果在网络上传输，或者要把内容保存在硬盘上，就要用到python的encode()函数把str转换为bytes，然后再做操作
# 6. 反之，如果从网络或磁盘上读取了字符流，那么读到的数据就是bytes，要把bytes变成str，就需要用到decode()函数
# 7. 在操作字符串时，经常遇到bytes与str的转换，为了避免乱码问题，应该始终坚持使用utf-8对两者进行转换
# 8.由于python源代码本身也是文本文件，所以保存源代码时务必指定保存为utf-8格式，所以一般要在源代码前面加上以下两行

#!/usr/bin/env python3 //这行注释告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*- //这行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

### python的list与tuple
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
# 1. list里面的元素的数据类型也可以不同，比如 L = ['Apple', 123, True];
# 2. list元素也可以是另一个list

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

### 判断语句

### 循环语句
# 1. 在循环中，break语句可以提前退出循环
# 2. break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用
# 3. 不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句
#    ，大多数情况可以调整循环逻辑去掉break和continue
# 4. python对缩进要求严格，无法用（）表示内在逻辑，用缩进表示

### dict和set
# 1. Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# 2. 注意：返回None的时候Python的交互式命令行不显示结果。
# 3. 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的
# 4. 和list比较，dict有以下特点：查找和插入的速度极快，不会随着key的增加而变慢；需要占用大量的内存，内存浪费多。
# 5. 而而而list相反：查找和插入的时间随着元素的增加而增加；占用空间小，浪费内存很少。
# 6. 所以，dict是用空间来换取时间的一种方法。
# 7. dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要
# ，需要牢记的第一条就是dict的key必须是不可变对象。
# 8. 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同
# ，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# 9. 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的
# ，因此，可以放心地作为key。而list是可变的，就不能作为key

## set
# 1. set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 2. 要创建一个set，需要提供一个list作为输入集合
# 3. 注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素
# ，显示的顺序也不表示set是有序的。。重复参数在set中自动被过滤
# 4. 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
# 5. set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
# 6. set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样
# ，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
# 使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

### 不变对象和可变对象

# 1. 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

# print("I\'m ok");
#
# print(True and True);
# =======================编码===========================
# age = 17;
# if age >= 18:
#     print("adult");
# else:
#     print("teenager");
# ==================================================
# print(ord("杜"));
# print('\u4e2d\u6587');
# ==================================================
# x = 'ABC';
# y = b'ABC';
# print(x.encode('utf-8'));#转为bytes   b‘ABC’
# print(y.decode('UTF-8'));#转为str     ’ABC‘’
# ==================================================
# s1 = 72;
# s2 = 85;
#
# r = (s2-s1)/s2;
# print('%.1f' % r);
# ==========================list========================
# classmates = ['Michael','Bob','Tracy'];
# # print(len(classmates));
# print(classmates[1]);
# print(classmates[-1]);# 取到最后一个元素
# print(classmates[len(classmates)-1]);# 取到最后一个元素
#
# classmates.append("Adam");# 追加元素到末尾
# classmates.insert(2,"Jack");# 插入元素到指定位置
#
# #classmates.pop(); # 删除末尾元素
# #classmates.pop(2); # 删除指定位置的元素
#
# classmates[1] = "Sarah"; # 直接替换元素
#
# print(classmates);
# =======================tuple===========================
# classmates = ("Michael","Bob","Tracy");
# print(classmates[1]);
# t = (); # 这是一个空的tuple
# t = (1,); # 定义只有1个元素的tuple,定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，
# # 又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# print(t);

# 定义一个可变的tuple
# t = ('a','b',['X','Y']);
# t[2][0] = 'A';
# t[2][1] = 'B';
# print(t);

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# print(L[0][1]);
# print(L[2][2]);
#
# print('%10s\n%10s\n%8s\n' % (L[0][1],L[1][1],L[2][2]));

# =======================判断语句===========================
# age = 13;
# if age >= 18:
#     print("your age is "+'%s' % age);
#     print('you are a adult');
# else:
#     print("your age is "+'%s' % age);
#     print('you are a teenager');

# age = 12;
# if age >=14 and age<18:
#     print('your age is'+'%s' % age);
#     print('you are a teenager');
# elif age >=0 and age <14:
#     print('your age is'+'%3s' % age);
#     print('you are a kid');
# else :
#     print("you are a adult");

# x = None;
# x = 0;
# x = '';
# x = '1';
# if x:
#     print("True"); # 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# else:
#     print("False");

# s = input('age:')
# s = int(s)
# if s>10:
#     print('你都'+'%s岁了' % s);
# else :
#     print('还不到10岁呢');
# =======================判断语句练习===========================

# height = 1.73;
# weight = 57;
#
# bmi = weight/(height * 2);
# if bmi < 18.5:
#     print('你的bmi为：%.2s\n最终评测结果为：偏瘦' % bmi);
# elif bmi < 25 and bmi > 18.5:
#     print('正常');
# elif bmi < 28 and bmi > 25:
#     print('偏胖');
# else:
#     print('太胖了');
# =======================循环语句练习===========================

# names = ('H','G','D','C','W');
# sum = 0;
# for name in names:
#     sum = ord(name)+sum;
# print(sum);

# i = list(range(101));
# sum = 0;
# for x in i:
#     sum = sum + x;
# print(sum);

# sum = 0;
# n = 101;
# while n > 0:
#     sum = sum+n;
#     n = n-2; # 所有奇数之和
# print(sum);

# L = ('A','D','S');
# for name in L:
#     if name == 'D':#break中断♻️
#         break;
#     print("Hello:%s!" % name);

# n = 0;
# while n <= 10:
#     n = n+1;
#     if n % 2 == 0:
#         continue #continue会🔚本轮♻️，直接执行⬇️1⃣轮
#     print(n);

# i = 10;
# while i > 5:
#     print('死循环');

# =======================dict和set===========================

# score = (12,32,6,36,87);
# names = {'D':score[0],'C':score[1],'X':score[2],'Z':score[3],'V':score[4]};
# name = 'H';
# # if(name in names): #通过 name in names判断要查询的key是否存在
# #     names[name] = 88;
# #     print(names[name]);
# # else:
# #     print('没有这个人哎～');
#
# # if names.get(name): #通过names.get(name)判断💊查询的key是否存在
# # # if names.get(name,-1);#如果📖不到key，可以🔙None或者自己🈯️定value
# #     print(names[name]);
# # else:
# #     print('没有这个人哎～');
#
# names.pop('D');
# print(names);

# s = set([1,1,2,3,4,4])
# s1 = set([3,4,5,7])
# s.add(10);
# s.remove(4);#通过remove(key)方法可以删除元素
# # print(s);
# print(s & s1); #交集
# print(s | s1); #并集

# l = [5,1,2,4]
# s = set(l)
# print(s) #打印出来的s里的内容

# a = 'abc'
# print(a.replace('a', 'AAAA'))
# print(a);

# S4 = set([1,(2,3),'abc'])
# print(S4)

# from day02 import my_abs
# print(my_abs('qw'))

