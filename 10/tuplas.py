
# * Tuplas are like lists
# x = ('Gleen', 'Sally', 'Joseph')
# print(x[2])
# y = (1, 9, 2)
# print(y)
# print(max(y))

# for iter in y:
#     print(iter)

# * but... TUples are "immutable"
# x = [9, 8, 7]
# x[2] = 6
# print(x)

# y = 'ABC'
# # y[2] = 'D' # ! TypeError

# z = (5, 4, 3)
# # z[2] = 0 # ! TypeErrorprint

# * A Tale of Two Sequences
# l = list()
# print(dir(l))
# t = tuple()
# print(dir(t))

# * Tuples and Assignment
# (x, y) = (4, 'fred')
# print(y)
# (a, b) = (99, 98)
# print(a)

# * Tuples and Dictionaries
# d = dict()
# d['csev'] = 2
# d['cswen'] = 4
# for (x, y) in d.items():
#     print(x, y)

# tups = d.items()
# print(tups)

# * Tuples are Comparable
print((0, 1, 2) < (5, 1, 2))
print((0, 1, 2000000) < (0, 3, 4))
print(('Jhone', 'Sally') < ('Jhones', 'Sam'))
print(('Jones', 'Sally') < ('Adams', 'Sam'))

