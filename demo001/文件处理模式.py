#f = open("test11.py","rb",encoding="utf-8")  #b的方式不能指定编码

# f = open('test11.py','rb') #b的方式不能指定编码
#
#
# data=f.read()
#
# print(data)
#
# print(data.decode('UTF-8'))
#
# f = open('test22.py','wb')
#
# f.write(bytes('1111111\n',encoding='utf-8'))
#
#
#
# f.write('你会'.encode('utf-8'))

# f = open('a.txt','w')
#
# print(f.close())
#
# f = open('a.txt',"r+",encoding="utf-8")
#
# # f.truncate(10)
#
# f = open('seek.txt','r',encoding='utf-8')
# print(f.tell())
# f.seek(10)
# print(f.tell())
# f.seek(3)
# print(f.tell())

f = open('日志文件','rb')

# for i in f.readlines():
#     print(i)


#循环文件推荐方式

# for i in f:
#     print(i)


#倒着读取文件内容
# for i in f:
#     #首先定义一个偏移量
#     offs = -10
#     #f.seek(-3,2)
#     while True:
#         f.seek(offs,2)
#         data = f.readlines()
#         if len(data) > 1:
#             print('文件的最后一行是%s' %(data[-1].decode('utf-8')))
#             break
#         offs*=2
#







