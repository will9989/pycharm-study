'''

    返回值：函数执行后，会调用方法的一个结果，结果就是返回值

    return:
        return后程序会直接停止
        1. 如果函数没有return，会回传None
        2. 写了return：    1. 后面不跟数据，仍回传None
                          2. return值，表示函数有一个返回值
                          3. return多个值，得到一个元组，元组存放所有返回值

'''

def func(a,b):
    return a + b

ret = func(10, 20)
print(ret)

