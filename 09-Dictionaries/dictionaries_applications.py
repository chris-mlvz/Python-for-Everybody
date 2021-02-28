
# * Many Counters with a Dictionary
# ccc = dict()
# ccc['csev'] = 1
# ccc['cwen'] = 1
# print(ccc)
# ccc['cwen'] = ccc['cwen'] + 1
# print(ccc)

# * Dictionary Tracebacks
# ccc = dict()
# # print(ccc['csev']) # ! KeyError
# print('csev' in ccc)

# * When we see a new name
# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)

# * The get method for dictionaries
# counts = {}
# name = 'csev'
# if name in counts:
#     x = counts[name]
# else:
#     x = 0

# x = counts.get(name, 0)

# * Simplified counting with get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
