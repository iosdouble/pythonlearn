# l = [1,2,3]
# for i in l:
#     print(i)
#
#
# x = 'hello'
# for a in x:
#     print(a)
#
#
# s = 'world'
# print(dir(s))
#
# iter_test = x.__iter__()
#
# print(iter_test)
# print(iter_test.__next__())
#
# l =[1,2,3]
#
# index = 0
# while index < len(l):
#     print(l[index])
#     index+=1;

# s = {1,2,3}
#
# for i in s:
#     print(i)

# dic = {'a':1,'b':2}
#
# iter_d = dic.__iter__();
#
# print(iter_d.__next__())
#
# l = [1,2,3,4,5]
#
# diedai_l = l.__iter__()
# while True:
#     try:
#         print(diedai_l.__next__())
#     except StopIteration:
#         print('迭代完毕，循环终止')
#         break

#
# l = ['die','erzi','sunzi','chongsunzi']
#
# iter_l = l.__iter__()
#
# # print(iter_l.__next__())
# # print(iter_l.__next__())
# # print(iter_l.__next__())
# # print(iter_l.__next__())
# # print(iter_l.__next__())
#
# print(next(iter_l))


# def test():
#     # return 1;
#     yield 1
#
# g = test()
# print(g)
#
# print(g.__next__())


#三元表达式

# name = 'nihui'
# res = 'SB' if name == 'alex' else '帅哥'
# print(res)

#列表解析

egg_list = []
for i in range(10):
    egg_list.append('鸡蛋%s' %i)
print(egg_list)

l = ['鸡蛋%s' %i for i in range(10)]
print(l)


ll = ['鸡蛋%s' %i for i in range(10) if i>5]
print(ll)


laomuji = ('鸡蛋%s' %i for i in range(10)) #生成器表达式
print(laomuji)

print(laomuji.__next__())
print(laomuji.__next__())

print(next(laomuji))

print(sum(i for i in range(1110001)))





