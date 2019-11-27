
# # Python 中定义函数的方式
#
# # def 定义函数的关键字
# # test 函数名
# # ():定义参数
# def test(x):
#     # 函数体
#     print("this is function")
#     x+=1
#     print(x)
# test(6)
#
#
#
# def test():
#     return 2*3+1;
#
# a = test()
# print(a)


# def test01():
#     message = 'this is test nihui'
#     print(message)
# def test02():
#     msg = "hello world!"
#     print(msg)
#     return msg
#
# def test03():
#     return 1,2,3,4,[123,12,"1321"],(213,"34"),{"nihui":"name","temp":(123,"test")}
#
# t1 = test01()
#
# t2 = test02()
#
# t3 = test03()
#
#
# print(t1)
#
# print(t2)
# print(t3)


# def calc(x,y):
#     res = x**y;
#     return res
#
# res = calc(2,3)
# print(res)


# def test(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# test(y=1,z=2,x=3)

# test(1,3,y=2)
# test(1,3,z=2,y=4)
# test(z=2,1,3)



# def handle(x,type="nihui"):
#     print(x)
#     print(type)
#
# handle("test")
# handle("test",type="hello")
# handle('hello',"world")

# def test(x,*args):
#     print(x)
#     print(args)
# test(1,2,3,4,5,6)


# def test(x,**kwargs):
#     print(x)
#     print(kwargs)
# test(1,y=2,z=3)
#
# # test(1,2,21,312,y=2,z=4)


def test(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)

test(123,123,123,123,{"nihui":"test","age":123},y=2,z=3)



