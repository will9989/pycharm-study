'''

参数：可以在函数调用的时候，给函数传递一些信息

分类：
    1. 形参，在函数定义的时候，需要准备一些变量来接收信息
        1. 位置参数
        2. 默认值参数， 在函数声明的时候给变量一个默认值，如果实参不传递信息，此默认值生效
        3. 动态传参
            1. *args, 表示接收所有的位置参数的动态传参
            2. **kwargs, 表示接收的所有关键字的动态传参

        顺序： 位置 > *args > 默认值 > **kwargs

    2. 实参
        1. 位置参数 按照输入位置传递参数
        2. 关键字参数    按照关键字的参数传递
        3. 混合参数
            顺序：位置参数放前面，混合参数放后面
        实参在执行的时候，需要保证形参有数据

'''

#
# def jisuan(a, opt, b):
#     if opt == "+":
#         print(a+b)
#     elif opt == "-":
#         print(a-b)
#     elif opt == "*":
#         print(a*b)
#     elif opt == "/":
#         print(a/b)
#     else:
#         print("no")

# def chi(zhu, fu, tang, tian):
#     print(zhu, fu, tang, tian)
#
# chi("米饭","番茄炒蛋","紫菜蛋花汤","哈根达斯")


# def luru(name, age, gender="男"):
#     print(name, age, gender)
#
# luru("张三", 18)
# luru("李四", 13)
# luru("王五", 23,"女")

# def chi(*food): # * 表示未知参数的动态传参，*接收到的值会统一放在元组里
#     print(food)
#
# chi("米饭","番茄炒蛋","紫菜蛋花汤","哈根达斯")

# def chi(**food): # ** 表示接收关键字的动态传参，**接收到的值会放在字典里
#     print(food)
#
# chi(fu="米饭",zhu="番茄炒蛋",tang="紫菜蛋花汤",tian="哈根达斯")


# def func(a, b, c="哈哈", *args, **kwargs):
#     print(a, b, c, args, kwargs)
#
# func(1,2,3,4,5,6,7,8,9,hello=456)

# def func(*args, **kwargs):  # 表示可以接收任何参数
#     print(args, kwargs)
#
# func()
# func(1)
# func(1,2,3,4,a=2,c=5)


# stu_lst = ["张三","李四","王五","陈六"]

# def func(*args):
#     print(args)
#
# func(*stu_lst)  #   *在实参位置，将列表打散成位置参数进行传递
#                 #   **则可以将字典传递


