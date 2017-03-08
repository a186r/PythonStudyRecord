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
