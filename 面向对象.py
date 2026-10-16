#ok依旧来补功课，补一下大一下学期本该掌握的内容
"""
Object-oriented Programming,简称（OOP），是一种编程范式
类：属性+方法(无顺序)
理解角度：封装、现实映射
创建类的对象的过程：类的实例化:类()-->对象(实例)
存在指针
.表示在个人/公共空间值里查找/写  （）表示调用
实例属性赋值：实例对象.属性名 = 值  向实例空间写入属性和值
实例对象.变量  查询顺序[实例空间值-->类空间值-->公共空间值]
"""
#声明类
class Lover:
    #属性
    head_num = 1
    has_heart = True
    love_Joe = True

    #方法
    def sajiao(self):
        print("撒娇ing")

    def happy(self):
        print("开心ing")

    def cry(self):
        print("哭ing")

    def kunhuo(self):
        print("困惑ing")

#实例化对象
shu = Lover()
joe = Lover()
# #（1）shu和joe是两个不同的对象，内存地址不同
# print(id(shu))
# print(id(joe))
# print(shu == joe)
# #(2)实例对象通过句点符号调用类的属性和方法
# print(shu.love_Joe)
# print(joe.love_Joe)
# shu.sajiao()
# shu.happy()
# #(3)调用类属性一定是同一个空间值
# print(id(shu.love_Joe))
# print(id(joe.love_Joe))
# print(id(shu.happy))
# print(id(joe.happy))

#实例属性
shu.name = "shu"
shu.age = 18
joe.age = 19
print(shu.name)
print(shu.age)

#(1)
shu.age = 19
print(shu.age)
print(joe.age)

#(2)实例对象.变量  查询顺序[实例空间值-->类空间值-->公共空间值]

"""
错误例子：
shu.happy = 1000
shu.happy()
"""
shu.happy()
shu.head_num = 2
print(shu.head_num)
print(joe.head_num)

print()