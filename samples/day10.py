#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 任何模块代码的第一行字符串都视为模块的文档注释
'a test module'

# 把作者导入进去，以后别人看到了，就只能仰视，仰视，仰视
__author__ = 'dursss'

# 以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。

# 从这里开始是正式的代码内容

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello %s!' % args[1])
    else:
        print('Too Many Arguments!')


if __name__ == '__main__':
    test()


# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试

# $ python3 hello.py
# Hello, world!
# $ python hello.py Michael
# Hello, Michael!

# 作用域 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，
# 有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的

def _private_1(name):
    return 'Hello ,%s' % name


def _private_2(name):
    return 'Hi ,%s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


        # 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，
        # 调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
        # 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。


        # 安装第三方模块
        # 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称
        # ，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
        #       pip3 install Pillow

        # Pillow是一个图片处理的库
