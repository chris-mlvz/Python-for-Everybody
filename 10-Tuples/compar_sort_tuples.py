
# * Sorting Lists of Tuples
# d = {'a': 10, 'b': 1, 'c': 22}
# print(d.items())
# print(sorted(d.items()))

# * Using sorted()
# d = {'a': 10, 'b': 1, 'c': 22}
# t = sorted(d.items())
# print(t)
# for k, v in sorted(d.items()):
#     print(k, v)

# * Sort by values instead of key
# c = {'a': 10, 'b': 1, 'c': 22}
# tmp = list()
# for k, v in c.items():
#     tmp.append((v, k))
# print(tmp)
# tmp = sorted(tmp, reverse=True)
# print(tmp)

# * The top 10 most common words
# fhand = open('romeo.txt')
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)

# lst = sorted(lst, reverse=True)

# for val, key in lst[:10]:
#     print(key, val)

# * EVen shorter Version
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v, k) for k, v in c.items()]))
