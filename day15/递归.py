

# def calc(n):
#     print(n)
#     calc(n)
# calc(10)


# def calc(n):
#     print(n)
#     if int(n/2) ==0:
#         return n
#     return calc(int(n/2))
# calc(10)


person_list = ["test1","test2","test3","test4"]

def ask_way(person_list):

    if len(person_list)==0:
        return '没人知道'

    person = person_list.pop(0)

    if person == 'test3':
        return '%s 知道' %person

    print('%s' %person + "不知道")

    res = ask_way(person_list)

    return res

print(ask_way(person_list))


