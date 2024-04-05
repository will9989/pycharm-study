'''
1. 文件操作

open(文件路径，mode="",encoding="")
    文件路径：
        1. 绝对路径
        2. 相对路径
    mode:
        r:read
        w:write
        a:append
        b:读写非文本文件

    with: 上下文，不需要手动关闭
'''

# 开启文档
# f = open("测试.txt", mode='r',encoding='utf*8')
#
# # content = f.read()  #全部读取
# # print(content)
#
# for line in f:
#     print(line.strip())

# 写入文档
# f = open("测试写入.txt",mode='w',encoding='utf-8')
# f.write("川菜")
#
# f.close()

# 循环写入文档
# lst = ['张无忌','小龙女','赵敏','刘备']
# f = open("打架.txt",mode='w',encoding='utf-8')
#
# for item in lst:
#     f.write(item)
#     f.write('\n')
#
# f.close()


# f = open("打架.txt",mode='a',encoding='utf-8')
# f.write("你好厉害")
#
# f.close()

# # with
# with open("测试.txt",mode="r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

# # 读取非文本文件
# with open("megumi.jpg",mode='rb') as f:
#     for line in f:
#         print(line)

# 文件复制
# with open("megumi.jpg",mode='rb') as f1,\
#     open ("./ceshifuzhi.jpg",mode='wb') as f2:
#     for line in f1:
#         f2.write(line)

# 文件修改
# 把文件中的周 ——》 张

import os

with open("名单.txt", mode="r", encoding="utf-8") as f1,\
    open("名单_测试.txt", mode="w", encoding="utf-8") as f2:
    for line in f1:
        line = line.strip()
        if line.startswith("周"):
            line = line.replace("周", "张")  #修改

        f2.write(line)
        f2.write("\n")
os.remove("名单.txt")
os.rename("名单_测试.txt","名单.txt")






