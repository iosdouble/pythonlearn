# 字典

#dict

# info={
#     "k1":"v1",
#     "k2":"v2"
# }
#
# info={
#     "k1":12,
#     "k2":True,
#     "k3":[11,22,33,{"kk1":"vv1"}],
#     "k4":(11,22,33,44)
# }


# info ={
#     1:"nihui",
#     "k1":"nihui",
#     True:"123",
#     # [12,13]:123,
#     ("tet","123"):"nihui",
#     {12,23}:"th"
# }
# print(info)

# info={
#     "k1":12,
#     "k2":True,
#     "k3":[11,22,33,{"kk1":"vv1"}],
#     "k4":(11,22,33,44)
# }
#
# print(info)



# info={
#     "k1":12,
#     "k2":True,
#     "k3":[11,22,33,{"kk1":"vv1"}],
#     "k4":(11,22,33,44)
# }
# # 获取键
# for item in info:
#     print(item)
#
# for item in  info.keys():
#     print(item)
# # 获取值
# for item in  info.values():
#     print(item)
#
# # 获取键值
# for item in info.items():
#     print(item)

# del  info["k1"]
# print(info)





# v = info["k1"]
# print(v)


# tempalte =" this is {name} age:{age}"
# v = tempalte.format(name="nihui",age=24)
# v1 = tempalte.format(**{"name":"nihui","age":12})
# print(v)
# print(v1)



# dict

# dic = {
#     "k1":"v1",
#     "k2":"v2"
# }
#
# v = "k1" in dic
# print(v)

# dic.update({"k1":"1231231","k3":123})
# print(dic)
#
# dic.update(k1 = 123,k3=213,k5="12321");
# print(dic)

# v = dic.setdefault("k1","123")
# print(dic)
# print(v)
#
# v1 = dic.setdefault("k3","456")
# print(dic)
# print(v1)


# v = dic.pop("k1")
# print(v)
#
# v1 = dic.popitem()
# print(v1)



# info={
#     "k1":12,
#     "k2":True,
#     "k3":[11,22,33,{"kk1":"vv1"}],
#     "k4":(11,22,33,44)
# }
#
# v = info["k1"]
# print(v)
#
# v1 = info.get("11111",123)
# print(v1)


# v = dict.fromkeys(["k1",123,"999"],123)
# print(v)



# v = info.copy();
# print(info)
# print(v)



# info.clear()
# print(info)






