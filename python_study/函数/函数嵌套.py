'''

函数可以嵌套函数

1. 函数可以作为返回值进行返回
2. 函数可以作为参数进行互相传递
函数名实际上就是一个变量名，表示一个内存地址

global:在局部，汇入全局变量
nonlocal:在局部，汇入上一层的局部变量

'''

# def func1():
#     b = 20
#     def func(): # 函数嵌套
#         pass

# def func():
#     def inner():
#         print(123)
#
#     return inner # 返回一个函数
#
# b1 = func() # b1是func的内部inner
# b1()

a = 10

# def func():
#     global a # 引入外部的全局变量
#     a = 20
#
# func()
# print(a)

def func():
    a = 10
    def func2():
        nonlocal a
        a = 20
    func2()
    print(a)

func()
