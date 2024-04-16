'''

闭包：内层函数对外层函数局部变量的使用
    1. 可以让一个变量常驻于内存
    2. 防止全局变量被修改（局部变量不能修改
    3. 函数名称可以当做变量进行赋值

'''

def func():
    a = 10
    def inner(): # 闭包
        nonlocal a

        a += 1
        return a
    return inner

ret = func() # 得到的返回值是内层函数
# inner执行时间不确定
# 要使该函数能正常执行，说明内层函数变量需要一直存在于内存中

r1 = ret()
print(r1)

r2 = ret()
print(r2)