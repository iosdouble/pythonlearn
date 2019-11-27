
# name = "nihui"
#
# # def chang_name():
# #     name = 'test'
# #     print('chang_name',name)
#
#
# def chang_name():
#     global name
#     name = "我真帅"
#     print("我的长相",name)
# chang_name();
# print(name)



# NAME = ["admin","zhangsan"]
#
# def admin():
#     # NAME = "nihui"
#     NAME = "lisi"
#     print(NAME)
#
# def test():
#     # NAME = "user"
#     NAME.append("wangwu")
#     print(NAME)
#
#
# admin()
# test()

# NAME = "admin"
#
# def nihui():
#     name = "nihui"
#     print(name)
#     def test():
#         name = "test"
#         print(name)
#         def user():
#             name = "user"
#             print(name)
#         print(name)
#         user()
#     test()
#     print(name)
# nihui()



name = "nihui"

def admin():
    name = '沉着'
    def test():
        global name
        name = "冷静"
    test()
    print(name)
print(name)
admin()
print(name)

