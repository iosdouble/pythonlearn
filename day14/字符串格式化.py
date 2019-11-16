
# msg = "I am %s my hobby is coding" %"nihui";
# msg1 = "I am %s my hobby is %s" % ("nihui","Python")
# msg2 = "I am %s my hobby is %s" % ("nihui",1)
# msg3 = "I am %s my hobby is %s" % ("nihui",[1,2])
#
# msg4 = "I am %s my hobby is %d" % ("nihui",12)
#
# print(msg)
# print(msg1)
# print(msg2)
# print(msg3)
# print(msg4)

# tpl = "percent %.2f" % 98.314241
# print(tpl)

# tpl = "percent %.4s" % 99.76444444444
# print(tpl)

# tpl = "I am %(name)s age %(age)d" % {"name":"nihui","age":18}
#
# tpl1 = "I am %(pp).2f" % {"pp":123.123534}
#
# print(tpl)
# print(tpl1)

# test = "I am {},age {},{}".format("nihui",23,"test")
# print(test)

# test = "I am {},age {},{}".format(*["nihui",23,"test"])
# print(test)

# test = "I am {0},age {2},{1}".format("nihui",23,"test")
# print(test)

# test = "I am {0},age {2},{1}".format(*["nihui",23,"test"])
# print(test)

# test = "I am {name},age {age},{test}".format(name="nihui",age=23,test="test")
# print(test)

# test = "I am {name},age {age},{test}".format(**{"name":"nihui","age":23,"test":"test"})
# print(test)

# test = "I am {1[0]} ,age {0[1]},i like {0[2]}".format([1,2,3],[11,22,33])
# print(test)


# test = "I am {:s} age {:d}, I Like {:f}".format("nihui",23,234.234)
# print(test)


# test = "I am {:s} age {:d}, I Like {:f}".format(*["nihui",23,234.234])
# print(test)

# test = "I am {name:s} age {age:d}, I Like {like:f}".format(**{"name":"nihui","age":23,"like":234.234})
# print(test)

number = "number {:b},{:o},{:d},{:x},{:X},{:%}".format(12,23,41,12,123,123,12312,2)
print(number)



