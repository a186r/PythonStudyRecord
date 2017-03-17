# 面向对象编程
# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name;
#         self.score = score;
#
#     def print_score(self):
#         print('%s:%s' % (self.name, self.score))
#
#
# # 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）。面向对象的程序写出来就像这样：
# bart = Student('Bart Simpson', 57)
# lisa = Student('Lisa Simpson', 93)
#
# print(bart.print_score())
# print(lisa.print_score())

# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
# Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，
# 比如，Bart Simpson和Lisa Simpson是两个具体的Student。
# 所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。
# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

# 数据封装、继承和多态是面向对象的三大特点

# 类和实例

# class Teacher(object):
#     pass
#
#
# bart = Teacher()
# bart.name = 'Bart Simpson'  # 可以自由的给变量绑定一个属性，比如，给bart绑定一个name
# print(bart.name)

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

# class Teacher(object):
#     def __init__(self, name, age, sex):  # 注意到init的第一个参数就是self，表示实例本身，所以可以把各个属性直接绑定到self，因为self就指向创建的实例本身
#         self.name = name
#         self.age = age
#         self.sex = sex
#         print('%s:%s:%s' % (self.name, self.sex, self.age))
#
#     def print_sex(self):
#         print(self.sex)
#
#
# # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
# bart = Teacher('dursss', '23', 'man')
# print(bart.name)
# print(bart.print_sex())

# 数据封装
# 面向对象的一个重要特点就是数据封装
# 但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，
# 可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法

# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
# bart = Student('Bart Simpson', 43)
# lisa = Student('Lisa Simpson', 36)
# bart.age = 8
# print(bart.age)
# print(lisa.age)

# 访问限制
# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。+
# 但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，
# 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print("%s:%s" % (self.__name, self.__score))
#
#
# bart = Student('Bart', 93)
# print(print(bart.__name))  # AttributeError: 'Student' object has no attribute '__name'

# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

print(200 / 1334)
