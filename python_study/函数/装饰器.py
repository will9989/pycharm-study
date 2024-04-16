'''

装饰器：本质上是一个闭包
    作用：在不改变原有函数调用的情况下，给函数增加新功能

    用户登录、日志
    雏形：
        def wrapper(fn): wrapper为装饰器，fn为目标函数
            def inner():
                # 在目标函数前....
                fn()
                # 在目标函数后....
                return ret
            return inner # 返回值为函数

        @wrapper
        def target():
            pass

        target() # => inner()

    一个函数可以被多个装饰器装饰
    @wrapper1
    @wrapper2
    def target:
        pass

    顺序：wrapper1.in => wrapper2.in => Target => wrapper2.out => wrapper1.out


'''

# def guanjia(test):
#     def inner():
#         print('开启')
#         test()
#         print('关闭')
#     return inner
#
# @guanjia # 相当于test1 = guanjia(test1)
# def test1():
#     print('测试1')
#
# @guanjia
# def test2():
#     print('测试2')
#
# # test1 = guanjia(test1) # 重新封装test1替换
# # test2 = guanjia(test2)
#
# test1() # 运行内层函数inner
# test2()

# def guanjia(test):
#     def inner(*args, **kwargs): # inner添加参数,args为元组，kwargs为字典
#         print('开启')
#         test(*args, **kwargs)
#         print('关闭')
#     return inner
#
# @guanjia # 相当于test1 = guanjia(test1)
# def test1(username, password):
#     print('登录',username, password)
#     print('测试1')
#
# @guanjia
# def test2(username, password, char):
#     print('登录',username, password, char)
#     print('测试2')
#
# # test1 = guanjia(test1) # 重新封装test1替换
# # test2 = guanjia(test2)
#
# test1("test","123456") # 运行内层函数inner
# test2("test","456789","ddd")

# def guanjia(test):
#     def inner(*args, **kwargs):
#         print('开启')
#         ret = test(*args, **kwargs) # 目标函数的执行，可拿到返回值
#         print('关闭')
#         return ret
#     return inner
#
# @guanjia # 相当于test1 = guanjia(test1)
# def test1(username, password):
#     print('登录',username, password)
#     print('测试1')
#     return "屠龙刀"
#
# @guanjia
# def test2(username, password, char):
#     print('登录',username, password, char)
#     print('测试2')
#
# # test1 = guanjia(test1) # 重新封装test1替换
# # test2 = guanjia(test2)
#
# ret = test1("test","123456") # 运行内层函数inner
# print(ret)
# test2("test","456789","ddd")


# # 装饰器嵌套
# def wrapper1(fn):   # fn:wrapper2.inner
#     def inner(*args, **kwargs):
#         print('这里是wrapper1 in')     # 1
#         ret = fn(*args, **kwargs)   #wrapper2.inner
#         print('这里是wrapper1 out')    # 5
#         return ret
#     return inner
#
# def wrapper2(fn):   # fn:target
#     def inner(*args, **kwargs):     # 2
#         print('这里是wrapper2 in')
#         ret = fn(*args, **kwargs)   # target
#         print('这里是wrapper2 out')    # 4
#         return ret
#     return inner
#
# @wrapper1   # target = wrapper1(wrapper2.inner) => target:wrapper1.inner
# @wrapper2   # target = wrapper2(target) => target：wrapper2.inner
# def target():
#     print('我是目标')   # 3
#
# target()
#
# # wrapper2函数被wrapper1装饰（包裹

login_flag = False

def login_verify(fn):
    def inner(*args, **kwargs):
        global login_flag
        print('请输入登录信息')
        if login_flag == False:
            while 1:
                username = input('>>>')
                password = input('>>>')
                if username == 'admin' and password =='123456':
                    print('登录成功')
                    login_flag = True
                    break
                else:
                    print('登录失败，用户名或密码错误')
        ret = fn(*args, **kwargs)
        return ret
    return inner

@login_verify
def add():
    print('添加员工信息')

@login_verify
def delete():
    print('删除员工信息')

@login_verify
def upd():
    print('更新员工信息')

@login_verify
def search():
    print('搜索员工信息')

add()
delete()
upd()
search()




