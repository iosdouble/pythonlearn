# set_A = [1,2,3,4]
# set_B = [2,3]
#
# A_and_B = []
# for itemA in set_A:
#     if itemA in set_B:
#         A_and_B.append(itemA)
#
# print(A_and_B)


set_A = [1,2,3,4,5]
set_B = [2,5,7,8]

a_set = set(set_A)
b_set = set(set_B)

print(a_set,b_set)

print(a_set.update(b_set))
print(a_set.update((2,4)))
print(a_set)

# print(a_set.symmetric_difference_update(b_set))
# print(a_set)
# print(b_set)

# print(a_set.issuperset(b_set))

# print(a_set.issubset(b_set))

# print(a_set.isdisjoint(b_set))


# print(a_set.intersection_update(b_set))
# print(a_set)
# print(b_set)

# print(a_set.difference_update(b_set))
# print(a_set)
# print(b_set)


# print(a_set.symmetric_difference(b_set))
# print(a_set^b_set)



# print(a_set.difference(b_set))
# print(a_set-b_set)


# print(a_set.union(b_set))
# print(a_set|b_set)



# print(a_set.intersection(b_set))
# print(b_set.intersection(a_set))
# print(a_set&b_set)


